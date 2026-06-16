import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

DB_USER     = "root"
DB_PASSWORD = quote_plus("Khu@nav@0472")
DB_HOST     = "localhost"
DB_NAME     = "weather_analytics"

engine = create_engine(
    f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
)

# Export all 3 tables to CSV
fact    = pd.read_sql("SELECT * FROM fact_weather", engine)
cities  = pd.read_sql("SELECT * FROM dim_city", engine)
dates   = pd.read_sql("SELECT * FROM dim_date", engine)

fact.to_csv("fact_weather.csv",   index=False)
cities.to_csv("dim_city.csv",     index=False)
dates.to_csv("dim_date.csv",      index=False)

print(f"✅ fact_weather.csv  — {len(fact)} rows")
print(f"✅ dim_city.csv      — {len(cities)} rows")
print(f"✅ dim_date.csv      — {len(dates)} rows")