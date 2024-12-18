import pandas as pd

def load_and_align_data(stock_file_path, news_file_path, output_file_path):    
    """
    Loads stock and news data, normalizes timestamps, and merges by date.

    Args:
        stock_file_path (str): Path to the stock data CSV file
        news_file_path (str): Path to the news data CSV file

    Returns:
        pd.DataFrame: Merged DataFrame with aligned dates
    """

    try:
        # Load stock and news data
        stock_df = pd.read_csv(stock_file_path)
        news_df = pd.read_csv(news_file_path)

        # Ensure consistent column names
        news_df.rename(columns={'date': 'Date'}, inplace=True)

        # Convert 'Date' columns to datetime
        stock_df['Date'] = pd.to_datetime(stock_df['Date'], errors='coerce')
        news_df['Date'] = pd.to_datetime(news_df['Date'], errors='coerce', utc=True)

        # Convert timezone-aware datetime to naive datetime by removing timezone info
        news_df['Date'] = news_df['Date'].dt.tz_localize(None)

        # Normalize timestamps to date only (removing time component)
        stock_df['Date'] = stock_df['Date'].dt.normalize()
        news_df['Date'] = news_df['Date'].dt.normalize()

        # Check for NaT values
        print(f"Number of NaT in stock_df: {stock_df['Date'].isna().sum()}")
        print(f"Number of NaT in news_df: {news_df['Date'].isna().sum()}")

        # Drop rows with NaT in 'Date' column due to conversion errors
        stock_df.dropna(subset=['Date'], inplace=True)
        news_df.dropna(subset=['Date'], inplace=True)

        # Print final types and head of DataFrames before merging
        print(f"Final Stock Date type: {stock_df['Date'].dtype}")
        print(f"Final News Date type: {news_df['Date'].dtype}")
        print(stock_df.head())
        print(news_df.head())

        # Merge datasets on 'Date'
        merged_df = pd.merge(stock_df, news_df, on='Date', how='inner')
        # Save merged DataFrame to CSV 
        merged_df.to_csv(output_file_path, index=False)
        print(f"Merged data saved to {output_file_path}") 

        return merged_df
    except Exception as e:
        print(f"Error loading or merging data: {e}")
        return None

# Example usage
stock_file_path = '../Data/yfinance_data/AMZN_historical_data.csv'
news_file_path = '../Data/raw_analyst_ratings.csv'
output_file_path = '../Data/merged_data.csv' 
merged_df = load_and_align_data(stock_file_path, news_file_path, output_file_path)
if merged_df is not None:
    print(merged_df.head())
else:
    print("Failed to merge data.")
