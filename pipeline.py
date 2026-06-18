from extract import run_extraction
from transform import transform
from load import reset_tables, load_dim_city, load_dim_date, load_fact
from datetime import datetime
from logger import logger
from report_generator import generate_report


def run_pipeline():
    print(f"\n{'=' * 50}")
    print(f"Pipeline started at {datetime.now()}")
    print(f"{'=' * 50}")

    logger.info("Pipeline Started")
    start_time = datetime.now()

    try:
        # Step 1: Extract
        raw_df = run_extraction()
        logger.info(f"Extracted {len(raw_df)} records")

        # Step 2: Transform
        clean_df = transform(raw_df)
        logger.info(
            f"Transformation completed successfully. Records: {len(clean_df)}"
        )

        # Step 3: Load
        reset_tables()

        city_dim = load_dim_city(clean_df)
        logger.info(f"dim_city loaded with {len(city_dim)} records")

        date_dim = load_dim_date(clean_df)
        logger.info(f"dim_date loaded with {len(date_dim)} records")

        load_fact(clean_df, city_dim, date_dim)
        logger.info("fact_weather loaded successfully")
        logger.info("========== ETL SUMMARY ==========")
        logger.info(f"Records Extracted: {len(raw_df)}")
        logger.info(f"Records Transformed: {len(clean_df)}")
        logger.info(f"Cities Loaded: {len(city_dim)}")
        logger.info(f"Dates Loaded: {len(date_dim)}")
        
        print(f"\nPipeline completed successfully at {datetime.now()}")
        end_time = datetime.now()
        run_time = end_time - start_time
        generate_report(
        len(raw_df),
        len(clean_df),
        len(city_dim),
        len(date_dim),
        run_time
    )
        logger.info(f"Pipeline Runtime: {run_time}")
        logger.info("Pipeline completed successfully")

    except Exception as e:
        print(f"\nPipeline failed: {e}")
        logger.exception("Pipeline Failed")

if __name__ == "__main__":
    run_pipeline()