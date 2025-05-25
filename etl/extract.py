"""
Extract module: retrieves weather data from a public API.
"""

import requests
import pandas as pd

def fetch_weather(lat: float, lon: float, start: str, end: str) -> pd.DataFrame:
    """
    Fetch hourly temperature and precipitation data from Open-Meteo API.
    - lat, lon: float coordinates
    - start, end: strings in 'YYYY-MM-DD'
    Returns a DataFrame with columns: time, temperature_2m, precipitation.
    """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m,precipitation",
        "start": f"{start}T00:00",
        "end": f"{end}T23:59",
        "timezone": "UTC"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    # Convert JSON hourly blocks into pandas DataFrame
    df = pd.DataFrame(data["hourly"])
    # Parse timestamp strings into pandas datetime objects
    df["time"] = pd.to_datetime(df["time"])
    return df
