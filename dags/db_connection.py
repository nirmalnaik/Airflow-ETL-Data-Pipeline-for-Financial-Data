import pandas as pd
import psycopg2

def insert_data_into_db(dataframe, connection):
    cursor = connection.cursor()
    for _, row in dataframe.iterrows():
        insert_query = """
        INSERT INTO stock_prices (date, open, high, low, close, volume, daily_change) VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (date) DO NOTHING;
        """
        cursor.execute(insert_query, (row['date'], row['open'], row['high'], row['low'], row['close'], row['volume'], row['daily_change']))
    
    connection.commit()  # Commit to save changes
    cursor.close()

def main():
    # Load the cleaned data
    df = pd.read_csv('dags/AAPL_daily_cleaned.csv')  # Ensure path is accessible by Airflow
    
    conn = None  # Initialize conn here to ensure it's in scope for the finally block
    try:
        conn = psycopg2.connect(
            dbname='financial_data',
            user='postgres',  # Replace with your actual username
            password='Dattu@123',  # Replace with your actual password
            host='localhost'  # Use 'host.docker.internal' if Airflow is running in Docker and you want to connect to the host's localhost
        )
        # Insert data into the database
        insert_data_into_db(df, conn)
        print("Data insertion successful.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if conn:
            conn.close()  # Ensure the connection is closed even if an error occurs

# If the script is executed directly, call the main function
if __name__ == "__main__":
    main()

