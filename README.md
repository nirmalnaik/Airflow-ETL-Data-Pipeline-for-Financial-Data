# Financial Data ETL Pipeline

This repository contains a financial data ETL (Extract, Transform, Load) pipeline, which is designed to automate the fetching, processing, and analysis of stock market data. The pipeline is orchestrated using Apache Airflow and includes several open-source tools for comprehensive data handling.

## Introduction

The pipeline automates the following tasks:

1. **Data Extraction**: Fetches daily stock market data.
2. **Data Transformation**: Cleans and transforms the data.
3. **Data Storage**: Stores the processed data in a PostgreSQL database.
4. **Data Analysis**: Performs financial analysis and generates visualizations.

## Data Source

Stock data is sourced from the Alpha Vantage API.

## Repository Contents

- `data_extraction.py` - Script to extract data from Alpha Vantage.
- `data_cleaning_transformation.py` - Script to clean and transform data.
- `db_connection.py` - Script for database operations with PostgreSQL.
- `stock_price_analysis.py` - Script for analyzing stock prices and plotting.
- `financial_data_pipeline.py` - Defines the Airflow DAG for the pipeline.
- `docker-compose.yaml` & `Dockerfile` - Docker configurations for Airflow.
- `AAPL_daily_data.csv` & `AAPL_daily_cleaned.csv` - Sample datasets.
- `Figure_1.png` - Sample output visualization.

## Getting Started

### Prerequisites

- Docker
- Alpha Vantage API key

### Installation

1. **Initialize Airflow**:
   ```bash
   docker-compose up airflow-init
2. **Start Airflow services**:
   ```bash
   docker-compose up
3. **Airflow Web UI**:
   Visit `http://localhost:8080` in your web browser. Default credentials are provided by Airflow.
4. **Build the Docker image:**:  
   Use the docker build command to create your image, assigning it a tag for easier reference.

   ```bash
   docker build -t custom-airflow:latest

## Usage

1. **Set Airflow Variables**:  
   Define your Alpha Vantage API key in the Airflow Web UI under Variables.

2. **Activate the DAG**:  
   Enable the `financial_data_pipeline` DAG and trigger its execution in the Airflow Web UI.

3. **Monitor Execution**:  
   Use the Airflow Web UI to monitor the DAG's execution and logs.
