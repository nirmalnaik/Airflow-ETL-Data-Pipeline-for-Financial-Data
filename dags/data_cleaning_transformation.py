import pandas as pd
import os

def clean_and_transform_data(file_path, output_file_path):
    try:
        # Load the dataset
        df = pd.read_csv(file_path)

        # Rename 'timestamp' column to 'date' for clarity, if it represents date
        df.rename(columns={'timestamp': 'date'}, inplace=True)

        # Convert 'date' to datetime format
        df['date'] = pd.to_datetime(df['date'])

        # Check and handle missing values
        if df.isnull().sum().any():
            print("Missing values detected. Handling missing values...")
            numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
            df[numerical_cols] = df[numerical_cols].fillna(df.mean())
            print("Missing values handled.")
        else:
            print("No missing values detected.")

        # Calculate daily price change
        df['daily_change'] = df['close'] - df['open']

        # Save the cleaned and transformed data to a new CSV file
        df.to_csv(output_file_path, index=False)
        print(f"Data cleaning and transformation completed successfully. Cleaned data saved to {output_file_path}")

    except Exception as e:
        print(f"An error occurred during data cleaning and transformation: {e}")

def main():
    # Define the file paths; these should be absolute paths when running in Airflow
    file_path = 'dags/AAPL_daily_data.csv'
    output_file_path = 'dags/AAPL_daily_cleaned.csv'

    # Call the clean and transform function
    clean_and_transform_data(file_path, output_file_path)

# If the script is executed directly, call the main function
if __name__ == "__main__":
    main()
