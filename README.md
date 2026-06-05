# FleetCap: Driver Capacity Forecasting Model & Dashboard

FleetCap is an operational planning and auditing tool that predicts whether driver capacity is sufficient to handle forecasted delivery demand in June 2026 based on May 2026 historical trip data.

Currently, it features forecast predictions and audits for **Berlin**, and provides historical profiles and simulated forecasts for other German cities (München, Frankfurt, Bielefeld, Düsseldorf, Hamburg, Heidelberg).

## Project Structure
* `index.html`: Interactive Light Mode dashboard (front-end).
* `preprocess.py`: Python preprocessing pipeline that categorizes the raw CSV delivery logs and parses the Excel forecast.
* `dashboard_data.json`: Consolidated, precalculated dataset containing forecast weeks and historical weekday profiles.
* `verify_data.py`: Audit verification script to check dataset integrity.
* `Dockerfile`: Lightweight Nginx server configuration to run the app in Docker.
* `default.conf`: Custom Nginx configuration listening on port `8089`.
* `docker-compose.yaml`: Docker Compose deployment specification.

## Core Forecasting Model & Calculations
For any 30-minute interval on weekday $w$ at time $t$ in June:

1. **Estimated Capacity ($C$)**:
   $$C = N \times P_{30}$$
   * $N$: Historical average of unique active drivers in May for weekday $w$ at time $t$.
   * $P_{30}$: Productivity rate in 30 minutes ($0.5 \times \text{Productivity per hour}$).

2. **Net Balance ($S$)**:
   $$S = C - D$$
   * $D$: Forecasted demand (number of deliveries) for that slot.

3. **Driver Requirements**:
   * If $S \ge 0$ (Sufficient capacity):
     $$\text{Excess Drivers} = \lfloor S / P_{30} \rfloor$$
   * If $S < 0$ (Deficit capacity):
     $$\text{Additional Drivers Needed} = \lceil |S| / P_{30} \rceil$$

## Docker Deployment (Port 8089)

To run the application locally or on a production server:

1. **Run using Docker Compose**:
   ```bash
   docker compose up -d
   ```

2. **Run using Standard Docker Commands**:
   ```bash
   docker build -t fleetcap-dashboard .
   docker run -d -p 8089:8089 --name fleetcap-container fleetcap-dashboard
   ```
   Access the dashboard at `http://localhost:8089/` or `http://<server-ip>:8089/`.
