from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import data_extraction
import data_cleaning_transformation
import db_connection
import stock_price_analysis

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 13),  # Adjust the start date to your needs
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'financial_data_pipeline',
    default_args=default_args,
    description='A DAG for processing financial data',
    schedule_interval=timedelta(days=1),  # This will run the DAG daily
)

t1 = PythonOperator(
    task_id='extract_data',
    python_callable=data_extraction.main,  # Make sure you have a main function in data_extraction.py
    dag=dag,
)

t2 = PythonOperator(
    task_id='clean_and_transform_data',
    python_callable=data_cleaning_transformation.main,  # Main function in data_cleaning_transformation.py
    dag=dag,
)

t3 = PythonOperator(
    task_id='load_data_to_db',
    python_callable=db_connection.main,  # Main function in db_connection.py to load data to Postgres
    dag=dag,
)

t4 = PythonOperator(
    task_id='analyze_data',
    python_callable=stock_price_analysis.main,  # Main function in stock_price_analysis.py
    dag=dag,
)

# Set the order of the tasks in your DAG
t1 >> t2 >> t3 >> t4
