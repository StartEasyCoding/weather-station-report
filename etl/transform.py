"""
Transform module: processes raw data into meaningful summaries.
"""

import pandas as pd

def process_weather(df: pd.DataFrame) -> pd.DataFrame:
    """
    Given an hourly weather DataFrame, compute per-day:
      - avg_temp: average temperature
      - max_temp: maximum temperature
      - min_temp: minimum temperature
      - total_precip: sum of precipitation
    Returns a DataFrame indexed by date.
    """
    # Extract date part for grouping
    df["date"] = df["time"].dt.date
    # Group by date and calculate aggregates
    daily = df.groupby("date").agg(
        avg_temp=pd.NamedAgg(column="temperature_2m", aggfunc="mean"),
        max_temp=pd.NamedAgg(column="temperature_2m", aggfunc="max"),
        min_temp=pd.NamedAgg(column="temperature_2m", aggfunc="min"),
        total_precip=pd.NamedAgg(column="precipitation", aggfunc="sum")
    ).reset_index()
    # Round values for readability
    for col in ["avg_temp", "max_temp", "min_temp", "total_precip"]:
        daily[col] = daily[col].round(2)
    return daily
