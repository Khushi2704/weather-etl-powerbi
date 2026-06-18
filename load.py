import pandas as pd
from urllib.parse import quote_plus
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()

# ── CONFIG ───────────────────────────────────────────
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD"))
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

engine = create_engine(
    f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
)

# ── STEP 1: DROP ALL TABLES CLEANLY ──────────────────
def reset_tables():
    with engine.connect() as conn:
        conn.execute(text("SET FOREIGN_KEY_CHECKS = 0"))
        conn.execute(text("DROP TABLE IF EXISTS fact_weather"))
        conn.execute(text("DROP TABLE IF EXISTS dim_city"))
        conn.execute(text("DROP TABLE IF EXISTS dim_date"))
        conn.execute(text("SET FOREIGN_KEY_CHECKS = 1"))
        conn.commit()
    print("Old tables dropped")

# ── STEP 2: LOAD DIM_CITY ────────────────────────────
def load_dim_city(df):
    cities = df[['city']].drop_duplicates().reset_index(drop=True)
    cities.columns = ['city_name']
    cities['country'] = 'IN'
    cities.insert(0, 'city_id', range(1, len(cities) + 1))

    cities.to_sql('dim_city', engine, if_exists='replace', index=False)
    print(f"dim_city loaded: {len(cities)} cities")
    return pd.read_sql("SELECT * FROM dim_city", engine)

# ── STEP 3: LOAD DIM_DATE ────────────────────────────
def load_dim_date(df):
    dates = df[['date', 'day_name', 'month',
                'month_name', 'quarter', 'year']].drop_duplicates().reset_index(drop=True)
    dates = dates.rename(columns={'date': 'full_date'})
    dates.insert(0, 'date_id', range(1, len(dates) + 1))

    dates.to_sql('dim_date', engine, if_exists='replace', index=False)
    print(f"dim_date loaded: {len(dates)} dates")
    return pd.read_sql("SELECT * FROM dim_date", engine)

# ── STEP 4: LOAD FACT_WEATHER ────────────────────────
def load_fact(df, city_dim, date_dim):
    df = df.merge(city_dim[['city_id', 'city_name']],
                  left_on='city', right_on='city_name')
    df = df.merge(date_dim[['date_id', 'full_date']],
                  left_on='date', right_on='full_date')

    fact = df[[
        'date_id', 'city_id', 'temp', 'humidity',
        'wind_speed', 'condition', 'feels_like', 'pressure'
    ]].copy()

    fact.columns = [
        'date_id', 'city_id', 'temp_celsius', 'humidity',
        'wind_speed', 'weather_condition', 'feels_like', 'pressure'
    ]

    fact.to_sql('fact_weather', engine, if_exists='replace', index=False)
    print(f"fact_weather loaded: {len(fact)} records")

# ── RUN ──────────────────────────────────────────────
if __name__ == "__main__":
    from extract import run_extraction
    from transform import transform

    raw_df   = run_extraction()
    clean_df = transform(raw_df)

    reset_tables()
    city_dim = load_dim_city(clean_df)
    date_dim = load_dim_date(clean_df)
    load_fact(clean_df, city_dim, date_dim)

    print("\nAll data loaded into MySQL successfully!")

    count = pd.read_sql("SELECT COUNT(*) as total FROM fact_weather", engine)
    print(f"Total rows in fact_weather: {count['total'][0]}")