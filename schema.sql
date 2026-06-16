CREATE DATABASE weather_analytics;

USE weather_analytics;

CREATE TABLE dim_city (
  city_id INT AUTO_INCREMENT PRIMARY KEY,
  city_name VARCHAR(50),
  country VARCHAR(10)
);

CREATE TABLE dim_date (
  date_id INT AUTO_INCREMENT PRIMARY KEY,
  full_date DATE,
  day_name VARCHAR(20),
  month INT,
  month_name VARCHAR(20),
  quarter INT,
  year INT
);

CREATE TABLE fact_weather (
  id INT AUTO_INCREMENT PRIMARY KEY,
  date_id INT,
  city_id INT,
  temp_celsius FLOAT,
  humidity INT,
  wind_speed FLOAT,
  weather_condition VARCHAR(100),
  feels_like FLOAT,
  pressure INT,
  FOREIGN KEY (date_id) REFERENCES dim_date(date_id),
  FOREIGN KEY (city_id) REFERENCES dim_city(city_id)
);