import os
import sys
import re
import json
import datetime
import pandas as pd
import numpy as np

# Reconfigure stdout to use UTF-8
sys.stdout.reconfigure(encoding='utf-8')

# Constants
CSV_PATH = "c:/Users/user/Desktop/analiza-3/driver-trip-activity.csv"
FORECAST_PATH = "c:/Users/user/Desktop/analiza-3/forcast.xlsx"
OUTPUT_JSON_PATH = "c:/Users/user/Desktop/analiza-3/dashboard_data.json"

CITIES = ["Berlin", "München", "Frankfurt", "Bielefeld", "Düsseldorf", "Hamburg", "Heidelberg"]

def classify_city(row):
    # Heuristic based on loading and arrival address
    loading = str(row['Loading Address']).lower()
    arrival = str(row['Arrival Address']).lower()
    
    if 'berlin' in loading or 'berlin' in arrival or '柏林' in loading or '柏林' in arrival:
        return 'Berlin'
    if 'münchen' in loading or 'münchen' in arrival or 'munich' in loading or 'munich' in arrival:
        return 'München'
    if 'frankfurt' in loading or 'frankfurt' in arrival:
        return 'Frankfurt'
    if 'bielefeld' in loading or 'bielefeld' in arrival:
        return 'Bielefeld'
    if 'düsseldorf' in loading or 'düsseldorf' in arrival or 'dusseldorf' in loading or 'dusseldorf' in arrival:
        return 'Düsseldorf'
    if 'hamburg' in loading or 'hamburg' in arrival:
        return 'Hamburg'
    if 'heidelberg' in loading or 'heidelberg' in arrival:
        return 'Heidelberg'
    
    return 'Other'

def process_historical_profiles():
    print("Loading CSV columns...")
    cols = ['Trip UUID', 'Nume Sofer', 'Trip Start Date', 'Trip Arrival', 'Loading Address', 'Arrival Address', 'Trip Status']
    df = pd.read_csv(CSV_PATH, escapechar='\\', usecols=cols)
    print(f"Loaded {len(df)} rows.")
    
    # Classify cities
    print("Classifying cities...")
    df['City'] = df.apply(classify_city, axis=1)
    print("City distribution:")
    print(df['City'].value_counts())
    
    # Filter out invalid rows (only completed trips, valid start/arrival dates)
    df = df[df['Trip Status'] == 'completed']
    df['Trip Start Date'] = pd.to_datetime(df['Trip Start Date'], errors='coerce')
    df['Trip Arrival'] = pd.to_datetime(df['Trip Arrival'], errors='coerce')
    df = df.dropna(subset=['Trip Start Date', 'Trip Arrival'])
    
    # May slots base date
    base_time = pd.Timestamp('2026-05-01 00:00:00')
    
    profiles = {}
    
    for city in CITIES:
        print(f"Generating profile for {city}...")
        df_city = df[df['City'] == city].copy()
        
        if len(df_city) == 0:
            print(f"Warning: No historical data for {city}")
            continue
            
        # Determine for each trip which 30-minute slots in May it overlaps
        # Slot index s represents slot: base_time + s * 30 mins
        # A trip overlaps slot s if trip_start < slot_end AND trip_arrival > slot_start
        # slot_start = base_time + s*30m, slot_end = base_time + (s+1)*30m
        
        # Calculate start slot index and end slot index for each trip
        start_offsets = (df_city['Trip Start Date'] - base_time).dt.total_seconds() / 1800.0
        arrival_offsets = (df_city['Trip Arrival'] - base_time).dt.total_seconds() / 1800.0
        
        # Clip to May boundaries (0 to 1487 slots)
        start_indices = np.maximum(0, np.floor(start_offsets).astype(int))
        # Subtract epsilon (1e-5) from arrival offset to avoid overlapping with next slot if arriving exactly on boundary
        arrival_indices = np.minimum(1487, np.floor(arrival_offsets - 1e-5).astype(int))
        
        # Create a list of expanded rows (slot_index, driver, trip_uuid)
        expanded_slots = []
        expanded_deliveries = []
        
        trip_drivers = df_city['Nume Sofer'].values
        trip_uuids = df_city['Trip UUID'].values
        trip_arrivals = df_city['Trip Arrival'].values
        
        start_indices_val = start_indices.values
        arrival_indices_val = arrival_indices.values
        
        # Track active drivers (overlap)
        for i in range(len(df_city)):
            drv = trip_drivers[i]
            s_idx = start_indices_val[i]
            e_idx = arrival_indices_val[i]
            # Add to all slots this trip overlaps with
            for s in range(s_idx, e_idx + 1):
                expanded_slots.append((s, drv))
                
            # Completed deliveries belong to the arrival slot
            arr_slot = int(np.floor((trip_arrivals[i] - base_time).total_seconds() / 1800.0))
            if 0 <= arr_slot <= 1487:
                expanded_deliveries.append((arr_slot, trip_uuids[i]))
                
        # Aggregate active drivers
        df_active = pd.DataFrame(expanded_slots, columns=['Slot_Index', 'Driver'])
        # Count unique drivers per slot
        active_per_slot = df_active.groupby('Slot_Index')['Driver'].nunique().reindex(range(1488), fill_value=0)
        
        # Aggregate completed deliveries
        df_deliv = pd.DataFrame(expanded_deliveries, columns=['Slot_Index', 'Trip'])
        deliv_per_slot = df_deliv.groupby('Slot_Index')['Trip'].count().reindex(range(1488), fill_value=0)
        
        # Map slot indices back to weekdays and times
        slot_datetimes = [base_time + datetime.timedelta(minutes=30 * s) for s in range(1488)]
        df_slots = pd.DataFrame({
            'Datetime': slot_datetimes,
            'Active_Drivers': active_per_slot,
            'Deliveries': deliv_per_slot
        })
        df_slots['Weekday'] = df_slots['Datetime'].dt.day_name()
        df_slots['Time'] = df_slots['Datetime'].dt.time.astype(str)
        
        # Calculate profile by Weekday and Time
        # Mean & Median active drivers, and Mean deliveries completed
        profile_df = df_slots.groupby(['Weekday', 'Time']).agg(
            Avg_Active_Drivers=('Active_Drivers', 'mean'),
            Median_Active_Drivers=('Active_Drivers', 'median'),
            Avg_Deliveries=('Deliveries', 'mean'),
            Max_Active_Drivers=('Active_Drivers', 'max')
        ).reset_index()
        
        # Format profile as dictionary: profiles[city][weekday][time] = { ... }
        city_profile = {}
        for _, row in profile_df.iterrows():
            wday = row['Weekday']
            t_str = row['Time'] # format: '18:30:00'
            # Format time to 'HH:MM'
            t_hm = t_str[:5]
            
            if wday not in city_profile:
                city_profile[wday] = {}
                
            city_profile[wday][t_hm] = {
                'active_drivers_mean': float(round(row['Avg_Active_Drivers'], 2)),
                'active_drivers_median': float(round(row['Median_Active_Drivers'], 2)),
                'deliveries_mean': float(round(row['Avg_Deliveries'], 2)),
                'active_drivers_max': int(row['Max_Active_Drivers'])
            }
            
        profiles[city] = city_profile
        
    return profiles

def parse_forecast_file():
    print("Parsing Excel forecast...")
    df = pd.read_excel(FORECAST_PATH)
    
    forecasts = {}
    
    # We will only parse for Berlin since it's the only one with forecast data.
    berlin_forecast = []
    
    # 5 weeks of forecast
    for w_idx in range(5):
        start_col = 2 + w_idx * 10
        end_col = start_col + 9 # Tot, Time, Monday...Sunday
        
        row1_vals = df.iloc[1, start_col:end_col].tolist()
        dates_raw = row1_vals[2:] # monday date to sunday date
        
        # Parse Dates
        dates = []
        for d in dates_raw:
            if isinstance(d, pd.Timestamp):
                dates.append(d.strftime('%Y-%m-%d'))
            elif isinstance(d, datetime.datetime):
                dates.append(d.strftime('%Y-%m-%d'))
            else:
                dates.append(str(d)[:10])
                
        # Parse slots
        data_rows = df.iloc[3:51, start_col:end_col]
        
        week_data = {}
        week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        
        for d_idx, day_name in enumerate(week_days):
            date_str = dates[d_idx]
            day_forecast = {}
            
            for _, r in data_rows.iterrows():
                # time column is index 1 of block
                t_val = r.iloc[1]
                if isinstance(t_val, datetime.time):
                    t_str = t_val.strftime('%H:%M')
                elif isinstance(t_val, str):
                    t_str = t_val[:5]
                else:
                    t_str = str(t_val)[:5]
                
                # order count is index 2+d_idx of block
                val = r.iloc[2 + d_idx]
                day_forecast[t_str] = int(val) if not pd.isna(val) else 0
                
            week_data[day_name] = {
                'date': date_str,
                'slots': day_forecast
            }
            
        berlin_forecast.append({
            'week_number': w_idx + 1,
            'days': week_data
        })
        
    forecasts['Berlin'] = berlin_forecast
    
    # Placeholder forecasts for other cities: set to null
    for city in CITIES:
        if city != 'Berlin':
            forecasts[city] = None
            
    return forecasts

def main():
    print("--- START PREPROCESSING ---")
    profiles = process_historical_profiles()
    forecasts = parse_forecast_file()
    
    output = {
        'cities': CITIES,
        'historical_profiles': profiles,
        'forecasts': forecasts
    }
    
    with open(OUTPUT_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
        
    print(f"\nSuccessfully created preprocessing output at: {OUTPUT_JSON_PATH}")
    print("Size of JSON file: {:.2f} KB".format(os.path.getsize(OUTPUT_JSON_PATH) / 1024.0))

if __name__ == "__main__":
    main()
