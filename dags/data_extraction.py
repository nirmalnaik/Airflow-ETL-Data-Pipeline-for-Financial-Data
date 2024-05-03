import requests
import os

def fetch_save_stock_data(symbol, api_key):
    base_url = "https://www.alphavantage.co/query"
    function = "TIME_SERIES_DAILY"
    outputsize = "compact"  # Use "full" for complete dataset
    datatype = "csv"  # Get data in CSV format

    query_params = {
        "function": function,
        "symbol": symbol,
        "apikey": api_key,
        "datatype": datatype,
        "outputsize": outputsize
    }

    response = requests.get(base_url, params=query_params)
    
    if response.status_code == 200:
        # Save the data to a file, assuming /opt/airflow/dags is your working directory for DAGs
        filepath = f"dags/{symbol}_daily_data.csv"
        with open(filepath, "wb") as file:
            file.write(response.content)
        print(f"Data for {symbol} saved successfully.")
    else:
        print("Failed to fetch data.")

def main():
    # Replace 'YOUR_API_KEY' with the actual API key and ensure it is securely managed
    api_key = 'Y76JAP165L7K937J'
    symbol = 'AAPL'
    fetch_save_stock_data(symbol, api_key)

if __name__ == "__main__":
    main()

