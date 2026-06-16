# 🌦️ Weather ETL Pipeline + Power BI Dashboard

## Project Overview
An automated ETL pipeline that extracts real-time weather data for 5 Indian cities, 
transforms it using Python, loads it into a MySQL star schema database, 
and visualizes KPIs in a Power BI dashboard.

## Tech Stack
- Python (Requests, Pandas, SQLAlchemy)
- MySQL (Star Schema — fact + 2 dimension tables)
- Power BI (DAX measures, drill-throughs)
- OpenWeather API
- Auto-scheduler (runs every 6 hours)

## Architecture
OpenWeather API → Python Extraction → Pandas Transformation → MySQL → Power BI

## Cities Tracked
Pune | Mumbai | Delhi | Bangalore | Chennai

## Key Features
- Extracts 200+ weather records across 5 cities
- Handles nulls, duplicates, and data quality flags
- Star schema optimized for Power BI relationships
- Pipeline auto-refreshes every 6 hours
