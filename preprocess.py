import os
import sys
import re
import json
import datetime
import glob
import pandas as pd
import numpy as np

# Reconfigure stdout to use UTF-8
sys.stdout.reconfigure(encoding='utf-8')

# Constants
CSV_PATH = "c:/Users/user/Desktop/analiza-3/driver-trip-activity.csv"
OUTPUT_JSON_PATH = "c:/Users/user/Desktop/analiza-3/dashboard_data.json"

# Define city mapping and keywords
CITY_METADATA = {
    'Berlin': ['berlin', '柏林'],
    'München': ['münchen', 'munich'],
    'Frankfurt': ['frankfurt'],
    'Bielefeld': ['bielefeld'],
    'Düsseldorf': ['düsseldorf', 'dusseldorf'],
    'Hamburg': ['hamburg'],
    'Heidelberg': ['heidelberg'],
    'Augsburg': ['augsburg'],
    'Karlsruhe': ['karlsruhe'],
    'Nürnberg': ['nürnberg', 'nuremberg'],
    'Potsdam': ['potsdam'],
    'Freiburg': ['freiburg'],
    'Ingolstadt': ['ingolstadt'],
    'Leipzig': ['leipzig'],
    'Heilbronn': ['heilbronn'],
    'Worms': ['worms'],
    'Ulm': ['ulm'],
    'Regensburg': ['regensburg'],
    'Gütersloh': ['gütersloh', 'guetersloh'],
    'Saarbrücken': ['saarbrücken', 'saarbruecken', 'saarbrucken']
}

def get_city_name_from_filename(filename):
    # Map filename to canonical city name
    base = os.path.splitext(os.path.basename(filename))[0].lower()
    if base == 'forcast':
        return 'Berlin'
    if base == 'berlin':
        return 'Berlin'
    if base == 'munich':
        return 'München'
    if base == 'nuremberg':
        return 'Nürnberg'
    if base == 'guetersloh':
        return 'Gütersloh'
    if base == 'dusseldorf':
        return 'Düsseldorf'
    if base == 'saarbruecken':
        return 'Saarbrücken'
    
    # Capitalize others
    for city in CITY_METADATA.keys():
        if base == city.lower():
            return city
            
    return base.capitalize()

def classify_city(row):
    loading = str(row['Loading Address']).lower()
    arrival = str(row['Arrival Address']).lower()
    
    # Check Berlin first (highest frequency)
    if 'berlin' in loading or 'berlin' in arrival or '柏林' in loading or '柏林' in arrival:
        return 'Berlin'
        
    for city, kws in CITY_METADATA.items():
        if city == 'Berlin':
            continue
        for kw in kws:
            if kw in loading or kw in arrival:
                return city
                
    return 'Other'

def parse_excel_date(d_val):
    if isinstance(d_val, (pd.Timestamp, datetime.datetime)):
        return d_val.strftime('%Y-%m-%d')
    d_str = str(d_val).strip()
    if not d_str or d_str.lower() == 'nan':
        return '2026-06-01' # Fallback
    
    # Clean timestamp suffix if present (e.g. ' 00:00:00')
    if ' ' in d_str:
        d_str = d_str.split(' ')[0]
        
    for fmt in ('%d/%m/%y', '%d/%m/%Y', '%Y-%m-%d', '%y-%m-%d'):
        try:
            return datetime.datetime.strptime(d_str, fmt).strftime('%Y-%m-%d')
        except ValueError:
            continue
            
    # Try parsing parts
    parts = re.split(r'[-/.]', d_str)
    if len(parts) == 3:
        # Check if year is first or last
        if len(parts[0]) == 4: # YYYY-MM-DD
            return f"{parts[0]}-{parts[1].zfill(2)}-{parts[2].zfill(2)}"
        elif len(parts[2]) == 4: # DD/MM/YYYY
            return f"{parts[2]}-{parts[1].zfill(2)}-{parts[0].zfill(2)}"
        elif len(parts[2]) == 2: # DD/MM/YY -> assume 20YY
            year = "20" + parts[2]
            return f"{year}-{parts[1].zfill(2)}-{parts[0].zfill(2)}"
            
    return d_str[:10]

def parse_forecast_file(file_path):
    try:
        xls = pd.ExcelFile(file_path)
        sheet = xls.sheet_names[0]
        df = pd.read_excel(file_path, sheet_name=sheet)
        
        # Check shape
        if df.shape[0] < 50 or df.shape[1] < 51:
            print(f"  Warning: {file_path} shape is too small {df.shape}. Treating as empty.")
            return None
            
        forecast_weeks = []
        # Parse 5 weeks (columns 2-10, 12-20, 22-30, 32-40, 42-50)
        for w_idx in range(5):
            start_col = 2 + w_idx * 10
            end_col = start_col + 9
            
            # Row 1 contains dates
            dates_row = df.iloc[1, start_col:end_col].tolist()
            dates_raw = dates_row[2:] # monday to sunday
            
            dates = [parse_excel_date(d) for d in dates_raw]
            
            # Row 3 to 50 contain values (48 slots)
            data_rows = df.iloc[3:51, start_col:end_col]
            
            week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            week_data = {}
            
            for d_idx, day_name in enumerate(week_days):
                date_str = dates[d_idx]
                day_forecast = {}
                
                for _, r in data_rows.iterrows():
                    # Time is index 1 of the block
                    t_val = r.iloc[1]
                    if isinstance(t_val, datetime.time):
                        t_str = t_val.strftime('%H:%M')
                    elif isinstance(t_val, str):
                        t_str = t_val.strip()[:5]
                    else:
                        t_str = str(t_val).strip()[:5]
                        
                    # Value is index 2 + d_idx
                    val = r.iloc[2 + d_idx]
                    try:
                        day_forecast[t_str] = int(float(val)) if not pd.isna(val) else 0
                    except:
                        day_forecast[t_str] = 0
                        
                week_data[day_name] = {
                    'date': date_str,
                    'slots': day_forecast
                }
                
            forecast_weeks.append({
                'week_number': w_idx + 1,
                'days': week_data
            })
            
        return forecast_weeks
    except Exception as e:
        print(f"  Error parsing {file_path}: {e}")
        return None

def process_historical_profiles(df, cities_to_process):
    # Filter out invalid rows (only completed trips, valid start/arrival dates)
    print("Filtering historical data for completed trips...")
    df_valid = df[df['Trip Status'] == 'completed'].copy()
    df_valid['Trip Start Date'] = pd.to_datetime(df_valid['Trip Start Date'], errors='coerce')
    df_valid['Trip Arrival'] = pd.to_datetime(df_valid['Trip Arrival'], errors='coerce')
    df_valid = df_valid.dropna(subset=['Trip Start Date', 'Trip Arrival'])
    
    # May slots base date
    base_time = pd.Timestamp('2026-05-01 00:00:00')
    
    profiles = {}
    
    for city in cities_to_process:
        print(f"Generating profile for {city}...")
        df_city = df_valid[df_valid['City'] == city].copy()
        
        if len(df_city) == 0:
            print(f"  Warning: No completed trips found for {city} in May. Creating empty profile.")
            # Create a profile with zeros
            city_profile = {}
            for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
                city_profile[day] = {}
                for h in range(24):
                    for m in ['00', '30']:
                        t_hm = f"{str(h).padStart(2, '0')}:{m}"
                        city_profile[day][t_hm] = {
                            'active_drivers_mean': 0.0,
                            'active_drivers_median': 0.0,
                            'deliveries_mean': 0.0,
                            'active_drivers_max': 0
                        }
            profiles[city] = city_profile
            continue
            
        # Fast overlapping slots calculation
        start_offsets = (df_city['Trip Start Date'] - base_time).dt.total_seconds() / 1800.0
        arrival_offsets = (df_city['Trip Arrival'] - base_time).dt.total_seconds() / 1800.0
        
        start_indices = np.maximum(0, np.floor(start_offsets).astype(int))
        arrival_indices = np.minimum(1487, np.floor(arrival_offsets - 1e-5).astype(int))
        
        expanded_slots = []
        expanded_deliveries = []
        
        trip_drivers = df_city['Nume Sofer'].values
        trip_uuids = df_city['Trip UUID'].values
        trip_arrivals = df_city['Trip Arrival'].values
        
        start_indices_val = start_indices.values
        arrival_indices_val = arrival_indices.values
        
        for i in range(len(df_city)):
            drv = trip_drivers[i]
            s_idx = start_indices_val[i]
            e_idx = arrival_indices_val[i]
            for s in range(s_idx, e_idx + 1):
                expanded_slots.append((s, drv))
                
            arr_slot = int(np.floor((trip_arrivals[i] - base_time).total_seconds() / 1800.0))
            if 0 <= arr_slot <= 1487:
                expanded_deliveries.append((arr_slot, trip_uuids[i]))
                
        df_active = pd.DataFrame(expanded_slots, columns=['Slot_Index', 'Driver'])
        active_per_slot = df_active.groupby('Slot_Index')['Driver'].nunique().reindex(range(1488), fill_value=0)
        
        df_deliv = pd.DataFrame(expanded_deliveries, columns=['Slot_Index', 'Trip'])
        deliv_per_slot = df_deliv.groupby('Slot_Index')['Trip'].count().reindex(range(1488), fill_value=0)
        
        slot_datetimes = [base_time + datetime.timedelta(minutes=30 * s) for s in range(1488)]
        df_slots = pd.DataFrame({
            'Datetime': slot_datetimes,
            'Active_Drivers': active_per_slot,
            'Deliveries': deliv_per_slot
        })
        df_slots['Weekday'] = df_slots['Datetime'].dt.day_name()
        df_slots['Time'] = df_slots['Datetime'].dt.time.astype(str)
        
        profile_df = df_slots.groupby(['Weekday', 'Time']).agg(
            Avg_Active_Drivers=('Active_Drivers', 'mean'),
            Median_Active_Drivers=('Active_Drivers', 'median'),
            Avg_Deliveries=('Deliveries', 'mean'),
            Max_Active_Drivers=('Active_Drivers', 'max')
        ).reset_index()
        
        city_profile = {}
        for _, row in profile_df.iterrows():
            wday = row['Weekday']
            t_str = row['Time'][:5]
            
            if wday not in city_profile:
                city_profile[wday] = {}
                
            city_profile[wday][t_str] = {
                'active_drivers_mean': float(round(row['Avg_Active_Drivers'], 2)),
                'active_drivers_median': float(round(row['Median_Active_Drivers'], 2)),
                'deliveries_mean': float(round(row['Avg_Deliveries'], 2)),
                'active_drivers_max': int(row['Max_Active_Drivers'])
            }
            
        profiles[city] = city_profile
        
    return profiles

def main():
    print("--- START DYNAMIC PREPROCESSING ---")
    
    # 1. Discover all xlsx forecast files in the workspace (excluding forcast.xlsx)
    xlsx_files = glob.glob("c:/Users/user/Desktop/analiza-3/*.xlsx")
    xlsx_files = [f for f in xlsx_files if 'forcast.xlsx' not in os.path.basename(f)]
    
    discovered_cities = {}
    for f in xlsx_files:
        c_name = get_city_name_from_filename(f)
        discovered_cities[c_name] = f
        
    print(f"Discovered {len(discovered_cities)} cities with forecast files:")
    for city, path in discovered_cities.items():
        print(f"  {city} -> {os.path.basename(path)}")
        
    # Standard cities list (include Berlin plus all discovered cities)
    active_cities = sorted(list(set(['Berlin'] + list(discovered_cities.keys()))))
    print(f"\nActive Cities List for Dashboard: {active_cities}")
    
    # Add keywords to CITY_METADATA dynamically for any city that isn't already there
    for city in active_cities:
        if city not in CITY_METADATA:
            CITY_METADATA[city] = [city.lower()]
            
    # 2. Load and Classify CSV
    print("\nLoading historical CSV dataset...")
    cols = ['Trip UUID', 'Nume Sofer', 'Trip Start Date', 'Trip Arrival', 'Loading Address', 'Arrival Address', 'Trip Status']
    df_csv = pd.read_csv(CSV_PATH, escapechar='\\', usecols=cols)
    print(f"Loaded {len(df_csv)} rows.")
    
    print("Classifying rows into cities...")
    df_csv['City'] = df_csv.apply(classify_city, axis=1)
    print("Classified city distributions:")
    print(df_csv['City'].value_counts())
    
    # 3. Process historical profiles
    profiles = process_historical_profiles(df_csv, active_cities)
    
    # 4. Parse Forecast Files
    print("\nParsing forecast files...")
    forecasts = {}
    for city in active_cities:
        # Get path
        path = discovered_cities.get(city)
        if not path and city == 'Berlin':
            # Fallback to check if forcast.xlsx exists
            if os.path.exists("c:/Users/user/Desktop/analiza-3/forcast.xlsx"):
                path = "c:/Users/user/Desktop/analiza-3/forcast.xlsx"
                
        if path:
            print(f"Parsing forecast for {city} from {os.path.basename(path)}...")
            f_data = parse_forecast_file(path)
            forecasts[city] = f_data
        else:
            print(f"No forecast file found for {city}.")
            forecasts[city] = None
            
    # 5. Output unified JSON
    output = {
        'cities': active_cities,
        'historical_profiles': profiles,
        'forecasts': forecasts
    }
    
    with open(OUTPUT_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
        
    print(f"\nSuccessfully created preprocessing output at: {OUTPUT_JSON_PATH}")
    print("Size of JSON file: {:.2f} KB".format(os.path.getsize(OUTPUT_JSON_PATH) / 1024.0))

if __name__ == "__main__":
    main()
