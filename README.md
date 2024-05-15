# Stock-Price-Prediction
This repository contains Python code for predicting stock prices using historical data and the Prophet library.

# Overview
The Stock Price Predictor is a Python script that forecasts stock prices based on historical data obtained from Yahoo Finance. It utilizes the Prophet library for time series forecasting. The script preprocesses the historical data, trains the Prophet model, and generates future price predictions. The predictions are then visualized alongside historical data for analysis.

# Features
*Data Retrieval*: Fetches historical stock data from Yahoo Finance using the `yfinance` library.
*Model Training*: Utilizes the Prophet library for time series forecasting, allowing customization of model parameters.
*Prediction Visualization**: Generates visualizations using Matplotlib and Seaborn to display historical data and predicted stock prices.
*Peak Annotation*: Automatically annotates maximum and minimum peaks in the predicted data for easy identification.
*Flexibility*: Designed to be easily extendable for predicting stock prices of various companies.

# Usage
1. Install the required Python dependencies listed in `requirements.txt`.
2. Create a file named `stocks.txt` containing the list of stock symbols to be analyzed, with each symbol on a new line.
3. Run the `main.py` script to initiate the stock price prediction process.
4. The predicted prices will be visualized and saved in the `Predictions` directory.
