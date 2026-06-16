from extract import run_extraction
from transform import transform
from load import reset_tables, load_dim_city, load_dim_date, load_fact
from datetime import datetime
import schedule
import time

def run_pipeline():
    print(f"\n{'='*50}")
    print(f" Pipeline started at {datetime.now()}")
    print(f"{'='*50}")

    try:
        # Step 1: Extract
        raw_df = run_extraction()

        # Step 2: Transform
        clean_df = transform(raw_df)

        # Step 3: Load
        reset_tables()
        city_dim = load_dim_city(clean_df)
        date_dim = load_dim_date(clean_df)
        load_fact(clean_df, city_dim, date_dim)

        print(f"\nPipeline completed successfully at {datetime.now()}")

    except Exception as e:
        print(f"\nPipeline failed: {e}")

# Run once immediately
run_pipeline()

# Then schedule every 6 hours
schedule.every(6).hours.do(run_pipeline)

print("\nScheduler running — pipeline will refresh every 6 hours")
print("Press Ctrl+C to stop\n")

while True:
    schedule.run_pending()
    time.sleep(60)