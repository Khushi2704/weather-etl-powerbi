import requests
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv

# ── CONFIG ──────────────────────────────────────────
load_dotenv()
API_KEY = os.getenv("API_KEY")
CITIES = ["Pune", "Mumbai", "Delhi", "Bangalore", "Chennai"]
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"

# ── EXTRACT FUNCTION ─────────────────────────────────
def extract_weather(city):
    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # catches HTTP errors
        data = response.json()

        records = []
        for item in data['list']:
            records.append({
                'city':            city,
                'datetime':        item['dt_txt'],
                'temp':            item['main']['temp'],
                'feels_like':      item['main']['feels_like'],
                'humidity':        item['main']['humidity'],
                'pressure':        item['main']['pressure'],
                'wind_speed':      item['wind']['speed'],
                'condition':       item['weather'][0]['description']
            })

        print(f"Extracted {len(records)} records for {city}")
        return pd.DataFrame(records)

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error for {city}: {e}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error for {city}: {e}")
        return pd.DataFrame()

# ── RUN EXTRACTION ───────────────────────────────────
def run_extraction():
    print(f"\nExtraction started at {datetime.now()}")
    all_data = pd.concat(
        [extract_weather(c) for c in CITIES],
        ignore_index=True
    )
    print(f"\nTotal records extracted: {len(all_data)}")
    print(all_data.head())
    return all_data

if __name__ == "__main__":
    df = run_extraction()