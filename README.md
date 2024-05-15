# Stock-Price-Prediction
This repository contains a simple Python code for preliminary prediction of stock prices using historical data and the Prophet library.

# Overview
The Stock Price Predictor is a Python script that forecasts stock prices based on historical data obtained from Yahoo Finance. It utilizes the Prophet library for time series forecasting. The script preprocesses the historical data, trains the Prophet model, and generates future price predictions. The predictions are then visualized alongside historical data for analysis.

# Features
1. *Data Retrieval*: Fetches historical stock data from Yahoo Finance using the `yfinance` library.
2. *Model Training*: Utilizes the Prophet library for time series forecasting, allowing customization of model parameters.
3. *Prediction Visualization*: Generates visualizations using Matplotlib and Seaborn to display historical data and predicted stock prices.
4. *Peak Annotation*: Automatically annotates maximum and minimum peaks in the predicted data for easy identification.

# Usage
1. Install the required Python dependencies listed in `requirements.txt`.
2. Create a file named `stocks.txt` containing the list of stock symbols to be analyzed, with each symbol on a new line.
3. Run the `main.py` script to initiate the stock price prediction process.
4. The predicted prices will be visualized and saved in the `Predictions` directory.

# Sample Outputs
![TCS_prediction](https://github.com/Vansh810/Stock-Price-Prediction/assets/90690711/9105aa51-d006-48ff-a357-2b413abc8fda)
![MRF_prediction](https://github.com/Vansh810/Stock-Price-Prediction/assets/90690711/88b41682-e8c8-41d1-890f-a5a71e3bd184)
![HDFCBANK_prediction](https://github.com/Vansh810/Stock-Price-Prediction/assets/90690711/99320335-6eb4-4bc9-8c37-a2899b8333ac)
