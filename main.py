"""
Smart Weather Station Report Generator
CLI to fetch weather data via Open-Meteo, process it, and generate a station report.
"""

import argparse
from etl.extract import fetch_weather
from etl.transform import process_weather
from etl.report import generate_report

def main():
    # Parse command-line arguments for station info and date range
    parser = argparse.ArgumentParser(description="Generate weather station report")
    parser.add_argument("--station-name", default="Station", help="Name of the weather station")
    parser.add_argument("--latitude", type=float, required=True, help="Station latitude")
    parser.add_argument("--longitude", type=float, required=True, help="Station longitude")
    parser.add_argument("--start-date", type=str, required=True, help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end-date", type=str, required=True, help="End date (YYYY-MM-DD)")
    args = parser.parse_args()

    # Extract raw hourly data
    raw_df = fetch_weather(args.latitude, args.longitude, args.start_date, args.end_date)
    # Transform into daily summaries
    summary_df = process_weather(raw_df)
    # Generate Markdown report and save to disk
    report_path = generate_report(args.station_name, args.latitude, args.longitude,
                                  summary_df, args.start_date, args.end_date)
    print(f"Report generated at {report_path}")

if __name__ == "__main__":
    main()
