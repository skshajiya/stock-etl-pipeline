import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine

# ----------------------
# EXTRACT
# ----------------------
def extract_data(ticker="AAPL"):
    stock = yf.Ticker(ticker)
    df = stock.history(period="1mo")
    df.reset_index(inplace=True)
    return df

# ----------------------
# TRANSFORM
# ----------------------
def transform_data(df):
    df = df.copy()

    df.columns = [col.lower() for col in df.columns]

    df['daily_return'] = (df['close'] - df['open']) / df['open']
    df['moving_avg_5'] = df['close'].rolling(5).mean()

    df = df.bfill()

    return df

# ----------------------
# LOAD (SQLite)
# ----------------------
def load_data(df):
    engine = create_engine("sqlite:///stock_data.db")

    df.to_sql(
        name="stock_prices",
        con=engine,
        if_exists="replace",
        index=False
    )

# ----------------------
# VALIDATE
# ----------------------
def validate_data(df):
    if df.isnull().sum().sum() > 0:
        print("❌ Missing values found")
    else:
        print("✅ Data clean")

# ----------------------
# MAIN
# ----------------------
if __name__ == "__main__":
    data = extract_data("AAPL")
    transformed = transform_data(data)
    validate_data(transformed)
    load_data(transformed)

    print("🎉 ETL Pipeline Completed!")