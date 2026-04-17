# stock-etl-pipeline
End-to-End Stock Data ETL Pipeline using Python, SQL, and Data Validation
# 📈 Stock Data ETL Pipeline

## 🚀 Overview
This project builds an end-to-end ETL pipeline to extract stock market data, transform it using Python, and load it into a SQL database.

## 🛠 Tech Stack
- Python
- Pandas
- yFinance API
- SQLite
- SQLAlchemy

## 🔄 ETL Pipeline
1. Extract stock data from API
2. Transform data (feature engineering, cleaning)
3. Load into SQL database
4. Perform analysis using SQL queries

## 📊 Features
- Multi-stock processing (AAPL, TSLA, MSFT)
- Moving average & daily return calculation
- Data validation checks
- SQL-based analytics

  ## 🧠 Advanced Features
- Incremental data loading
- Modular ETL architecture
- Logging for monitoring pipeline
- Interactive dashboard using Streamlit

## ▶️ How to Run
```bash
pip install pandas yfinance sqlalchemy
python etl_pipeline.py
