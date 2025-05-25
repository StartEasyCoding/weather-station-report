# Smart Weather Station Report

A simple Python project to fetch weather data from Open-Meteo, process it, and generate a Markdown report.

## Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/StartEasyCoding/weather-station-report.git
   cd weather-station-report
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main script with coordinates and dates:
```bash
python main.py \
  --station-name "New York City" \
  --latitude 40.7128 \
  --longitude -74.0060 \
  --start-date 2023-08-01 \
  --end-date 2023-08-07
```

The report will be saved under `reports/` as a Markdown file.

## Notes

- **Extract**: uses `requests` to call Open-Meteo (no API key needed).
- **Transform**: aggregates hourly data into daily metrics.
- **Report**: outputs a clean Markdown table for easy reading.
