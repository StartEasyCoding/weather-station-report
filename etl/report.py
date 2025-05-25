"""
Report module: generates a Markdown report from processed data.
"""

import os

def generate_report(station: str, lat: float, lon: float, df, start: str, end: str) -> str:
    """
    Create a Markdown report for the given station and date range.
    - station: station name
    - lat, lon: coordinates
    - df: DataFrame with daily summaries
    - start, end: period strings
    Returns the file path of the generated report.
    """
    os.makedirs("reports", exist_ok=True)
    filename = f"{station.replace(' ', '_')}_{start}_{end}.md"
    filepath = os.path.join("reports", filename)
    with open(filepath, "w") as f:
        f.write(f"# Weather Report for {station}\n\n")
        f.write(f"- **Location:** {lat}, {lon}\n")
        f.write(f"- **Period:** {start} to {end}\n\n")
        f.write("| Date | Avg Temp (°C) | Max Temp (°C) | Min Temp (°C) | Total Precip (mm) |\n")
        f.write("|------|---------------|---------------|---------------|------------------|\n")
        # Write each day's summary row
        for _, row in df.iterrows():
            f.write(f"| {row['date']} | {row['avg_temp']} | {row['max_temp']} | {row['min_temp']} | {row['total_precip']} |\n")
    return filepath
