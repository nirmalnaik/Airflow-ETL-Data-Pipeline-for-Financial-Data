import pandas as pd
import psycopg2
import matplotlib.pyplot as plt

def fetch_stock_prices(connection_params):
    conn = None
    try:
        conn = psycopg2.connect(**connection_params)
        query = "SELECT date, close FROM stock_prices ORDER BY date ASC;"
        df = pd.read_sql_query(query, conn)
        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        return pd.DataFrame()
    finally:
        if conn:
            conn.close()

def plot_stock_prices(df_stock):
    if not df_stock.empty:
        df_stock['date'] = pd.to_datetime(df_stock['date'])
        df_stock['30_day_moving_avg'] = df_stock['close'].rolling(window=30).mean()
        output_filepath = 'dags/AAPL_stock_plot.png'

        plt.figure(figsize=(14, 7))
        plt.plot(df_stock['date'], df_stock['close'], label='Daily Closing Price', alpha=0.5)
        plt.plot(df_stock['date'], df_stock['30_day_moving_avg'], label='30-Day Moving Average', color='red', linewidth=2)
        plt.title('AAPL Stock Price and 30-Day Moving Average')
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        plt.savefig(output_filepath)
        plt.close()
    else:
        print("No data available for analysis.")

def main():
    connection_params = {
        'dbname': 'financial_data',
        'user': 'postgres',
        'password': 'Dattu@123',
        'host': 'localhost'
    }

    df_stock = fetch_stock_prices(connection_params)
    plot_stock_prices(df_stock)

if __name__ == "__main__":
    main()
