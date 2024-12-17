import pandas as pd

def load_and_verify_csv(file_path, required_columns=['Open', 'High', 'Low', 'Close', 'Volume']):
    """
    Load CSV data into a DataFrame and verify required columns are present.

    Parameters:
    - file_path (str): Path to the CSV file
    - required_columns (list): List of required columns

    Returns:
    - DataFrame: Loaded DataFrame if all required columns are present
    - None: If any required column is missing
    """
    try:
        df = pd.read_csv(file_path)

        # Verify required columns
        if all(column in df.columns for column in required_columns):
            print("All required columns are present.")
            return df
        else:
            missing_columns = [column for column in required_columns if column not in df.columns]
            print(f"Missing columns: {missing_columns}")
            return None
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return None

# Example usage
file_path = '../../../AMZN_historical_data.csv'
df = load_and_verify_csv(file_path)
if df is not None:
    print(df.head())
