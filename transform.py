import pandas as pd
from extract import run_extraction

# ── TRANSFORM FUNCTION ───────────────────────────────
def transform(df):
    print("\nStarting transformation...")
    print(f"Records before cleaning: {len(df)}")

    # 1. Convert datetime
    df['datetime'] = pd.to_datetime(df['datetime'])

    # 2. Remove duplicates
    df.drop_duplicates(subset=['city', 'datetime'], inplace=True)

    # 3. Handle nulls
    df['temp'].fillna(df['temp'].mean() )
    df['humidity'].fillna(df['humidity'].median() )
    df['wind_speed'].fillna(0 )
    df['condition'].fillna('Unknown')

    # 4. Feature engineering
    df['date']       = df['datetime'].dt.date
    df['hour']       = df['datetime'].dt.hour
    df['day_name']   = df['datetime'].dt.day_name()
    df['month']      = df['datetime'].dt.month
    df['month_name'] = df['datetime'].dt.month_name()
    df['quarter']    = df['datetime'].dt.quarter
    df['year']       = df['datetime'].dt.year

    # 5. Temperature category
    df['temp_category'] = pd.cut(
        df['temp'],
        bins=[-10, 15, 25, 35, 50],
        labels=['Cold', 'Mild', 'Warm', 'Hot']
    )

    # 6. Data quality flag
    df['is_valid'] = (
        df['temp'].between(-50, 60) &
        df['humidity'].between(0, 100) &
        df['wind_speed'].between(0, 200)
    )

    print(f"Records after cleaning: {len(df)}")
    print(f"Valid records:   {df['is_valid'].sum()}")
    print(f"Invalid records: {(~df['is_valid']).sum()}")
    print(f"\nSample transformed data:")
    print(df[['city','datetime','temp','humidity',
              'temp_category','day_name','is_valid']].head())

    return df

# ── RUN ──────────────────────────────────────────────
if __name__ == "__main__":
    raw_df = run_extraction()
    clean_df = transform(raw_df)