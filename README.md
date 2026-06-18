# Weather ETL Analytics Pipeline

## Project Overview

This project is an end-to-end Weather ETL (Extract, Transform, Load) Pipeline built using Python, MySQL, and Power BI. The pipeline extracts weather forecast data from the OpenWeather API, performs data cleaning and transformation, loads the processed data into a MySQL data warehouse, and visualizes insights through an interactive Power BI dashboard.

The project demonstrates data engineering concepts such as ETL automation, data warehousing, logging, reporting, and secure configuration management.

---

## Tech Stack

* Python
* Pandas
* OpenWeather API
* MySQL
* SQLAlchemy
* Power BI
* Git & GitHub

---

## Project Architecture

OpenWeather API

↓

Extract Layer (extract.py)

↓

Transform Layer (transform.py)

↓

Load Layer (load.py)

↓

MySQL Data Warehouse

↓

Power BI Dashboard

---

## Features

### Data Extraction

* Extracts 5-day weather forecast data from OpenWeather API
* Collects weather information for multiple Indian cities
* Handles API requests and response processing

### Data Transformation

* Removes duplicate records
* Handles missing values
* Converts datetime fields
* Creates derived features such as:

  * Temperature Category
  * Day Name
  * Data Validation Flag

### Data Loading

* Loads data into MySQL
* Implements a Star Schema design
* Creates and populates:

  * Dim_City
  * Dim_Date
  * Fact_Weather

### Monitoring & Automation

* ETL execution logging
* Runtime tracking
* ETL summary reporting
* Error handling and exception logging

### Security

* Environment variables stored in `.env`
* API keys hidden from source code
* Database credentials secured
* Sensitive files excluded using `.gitignore`

---

## Database Schema

### Dimension Tables

#### Dim_City

Stores city information.

| Column    |
| --------- |
| city_id   |
| city_name |

#### Dim_Date

Stores date-related attributes.

| Column    |
| --------- |
| date_id   |
| full_date |
| day_name  |

### Fact Table

#### Fact_Weather

| Column              |
| ------------------- |
| date_id             |
| city_id             |
| temperature_celsius |
| humidity            |
| wind_speed          |
| weather_condition   |
| feels_like          |
| pressure            |

---

## Logging and Reporting

The project includes:

### Logging

All ETL activities are logged to:

weather-pipeline.log

Examples:

* Pipeline Started
* Records Extracted
* Records Loaded
* Pipeline Runtime
* Errors and Exceptions

### ETL Report

A summary report is automatically generated after successful execution.

Example Metrics:

* Records Extracted
* Records Transformed
* Cities Loaded
* Dates Loaded
* Pipeline Runtime

---

## Power BI Dashboard

The dashboard provides:

* Temperature Analysis
* Humidity Trends
* Weather Condition Distribution
* City-wise Weather Insights
* Interactive Filtering

(Add dashboard screenshots here)

---

## Project Structure

weather-etl-powerbi/

├── extract.py

├── transform.py

├── load.py

├── pipeline.py

├── logger.py

├── report_generator.py

├── schema.sql

├── README.md

├── .gitignore

├── .env (excluded from GitHub)

└── weather-analytics.pbix

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone <repository_url>
cd weather-etl-powerbi
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file:

```env
API_KEY=your_api_key

DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_NAME=weather_analytics
```

### 4. Run Pipeline

```bash
python pipeline.py
```

---

## Key Learnings

* ETL Pipeline Development
* Data Cleaning and Transformation
* Data Warehousing Concepts
* Star Schema Design
* Python Automation
* Logging and Monitoring
* Environment Variable Management
* Power BI Reporting

---

## Future Enhancements

* Email Notifications
* Cloud Deployment (AWS/Azure)
* Historical Weather Storage
* Scheduling with Airflow
* Real-Time Weather Streaming

---

## Author

Khushi

B.Tech Computer Science Engineering

Aspiring Data Analyst | Python | SQL | Power BI | Data Engineering
