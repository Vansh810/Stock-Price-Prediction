from prophet import Prophet
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
import yfinance as yf
import seaborn as sns
import os


def download_stock_data(stock_symbol, start_date, end_date):
    try:
        # Append ".NS" to the stock symbol for NSE data
        symbol = stock_symbol + ".NS"

        # Download historical stock data within the specified date range
        stock_data = yf.download(symbol, start=start_date, end=end_date)

        return stock_data
    except Exception as e:
        print(f"Error downloading data for {stock_symbol}: {e}")
        return None


def has_growth(stock_data):
    # Check if there's sufficient data
    if len(stock_data) < 2:
        return False

    # Calculate the overall percentage change in the Close prices
    percentage_change = stock_data['Close'].pct_change()

    # If the mean percentage change is positive, consider it as growth
    return percentage_change.mean() > 0


def predict_stock_price(stock_data):
    try:
        # Check if there's growth in the data
        growth = has_growth(stock_data)

        # Prepare the data for Prophet
        df = stock_data.reset_index()
        df = df.rename(columns={'Date': 'ds', 'Close': 'y'})

        # Initialize and fit the model
        model = Prophet(
            weekly_seasonality=False,
            changepoint_prior_scale=0.75,
            yearly_seasonality=True,
            daily_seasonality=True,
            n_changepoints=50
        )

        # Add country holidays
        model.add_country_holidays(country_name='IND')

        # Add a growth component if growth is detected
        if growth:
            model.add_seasonality(name='custom_growth', period=90, fourier_order=20)

        model.fit(df)

        # Make future dataframe for predictions (limit to 1 year)
        future = model.make_future_dataframe(periods=365)  # 365 days for next year

        # Predict stock prices
        forecast = model.predict(future)

        return forecast
    except Exception as e:
        print(f"Error predicting stock price: {e}")
        return None


def plot_stock_data_and_forecast(stock_data, forecast, stock_symbol):
    # Calculate historical start date as one month before the current date
    end_date = datetime.now()
    historical_start_date = end_date - timedelta(days=30)

    # Filter data to include only historical data from historical_start_date to end_date
    filtered_data = stock_data[
        (stock_data.index >= historical_start_date) &
        (stock_data.index <= end_date)
    ]

    # Plot historical data
    plt.figure(figsize=(12, 6))
    ax = sns.lineplot(x=filtered_data.index, y=filtered_data['Close'], label='Historical Data')

    # Calculate forecast start date as the next day after the current date
    forecast_start = end_date - timedelta(days=30)

    # Calculate forecast end date as one year from the current date
    forecast_end = end_date + timedelta(days=365)

    # Plot predicted values from forecast_start to forecast_end
    filtered_forecast = forecast[
        (forecast['ds'] >= forecast_start) &
        (forecast['ds'] <= forecast_end)
    ]
    sns.lineplot(x=filtered_forecast['ds'], y=filtered_forecast['yhat'], label='Predicted Data', color='red')

    # Find max and min peaks
    max_date = filtered_forecast.loc[filtered_forecast['yhat'].idxmax()]['ds']
    max_value = filtered_forecast['yhat'].max()

    min_date = filtered_forecast.loc[filtered_forecast['yhat'].idxmin()]['ds']
    min_value = filtered_forecast['yhat'].min()

    # Highlight max and min peaks
    ax.scatter(max_date, max_value, color='green', marker='^', label='Max Peak')
    ax.scatter(min_date, min_value, color='red', marker='v', label='Min Peak')

    # Display y-values and dates on the right side
    current_date = datetime.now()

    max_peak_annotation_date = (current_date + timedelta(days=(max_date - forecast_start).days)).strftime("%Y-%m-%d")
    min_peak_annotation_date = (current_date + timedelta(days=(min_date - forecast_start).days)).strftime("%Y-%m-%d")

    max_peak_annotation = f'Max Peak: {max_value:.2f} ({max_peak_annotation_date})'
    min_peak_annotation = f'Min Peak: {min_value:.2f} ({min_peak_annotation_date})'

    ax.annotate(max_peak_annotation, xy=(1, 0.95), xycoords='axes fraction', ha='left', va='top', color='green')
    ax.annotate(min_peak_annotation, xy=(1, 0.9), xycoords='axes fraction', ha='left', va='top', color='red')

    plt.title(f"Stock Symbol: {stock_symbol}")
    plt.xlabel("Date")
    plt.ylabel("Close Price")
    plt.legend()
    plt.tight_layout(rect=(0, 0, 0.8, 1))  # Adjust layout for the annotations
    output_path = os.path.join('Predictions', f'{stock_symbol}_prediction.png')
    plt.savefig(output_path)
    plt.close()

    print(f"Plot saved to: {output_path}")


def main():
    # Calculate start and end dates dynamically
    end_date = datetime.now()
    end_date_str = end_date.strftime('%Y-%m-%d')
    start_date = (end_date - timedelta(days=5 * 365)).strftime('%Y-%m-%d')

    # Get a list of stock symbols from the user
    with open('stocks.txt', 'r') as file:
        stock_symbols = file.read().splitlines()

    for symbol in stock_symbols:
        # Download stock data
        stock_data = download_stock_data(symbol, start_date, end_date_str)

        if stock_data is not None:
            # Predict stock prices with automatic growth detection
            forecast = predict_stock_price(stock_data)

            if forecast is not None:
                # Plot historical data and forecast
                plot_stock_data_and_forecast(stock_data, forecast, symbol)


if __name__ == "__main__":
    main()
