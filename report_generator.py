from datetime import datetime

def generate_report(raw_records,
                    transformed_records,
                    cities_loaded,
                    dates_loaded,
                    runtime):

    with open("daily_report.txt", "w") as report:

        report.write("WEATHER ETL DAILY REPORT\n")
        report.write("=" * 40 + "\n\n")

        report.write(f"Generated On: {datetime.now()}\n\n")

        report.write(f"Records Extracted: {raw_records}\n")
        report.write(f"Records Transformed: {transformed_records}\n")
        report.write(f"Cities Loaded: {cities_loaded}\n")
        report.write(f"Dates Loaded: {dates_loaded}\n")
        report.write(f"Pipeline Runtime: {runtime}\n")