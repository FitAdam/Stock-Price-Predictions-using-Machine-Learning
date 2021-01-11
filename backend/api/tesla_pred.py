# Import your packages
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA

stock = pd.read_csv('TESLAHistoricalQuotes.csv', sep=',')
# Drop first observation because it did not have a date
stock = stock.drop(0,0)
# Convert your date to datetime object
stock.date = pd.to_datetime(stock.date)
# Sort them by date with oldest first
stock = stock.sort_values('date')
# Set the index to date
stock.set_index(stock.date, inplace=True)
stock = stock.drop('date', 1)

# Build your model
# We use an autoregression of 1 (1 day lag), and 0 for differencing (subtracting previous observations for stationarity), and 3 (day lag) for our moving average
mod = ARIMA(stock.close, order=(1,0,3))
# Fit your model
results = mod.fit()
# Print a bunch over informatino about your model
results.summary()

# Create and plot your predictions!
stock['forecast'] = results.predict(dynamic=False)
# Note, dynamic=False means that it will make every prediction by accounting for all observations prior to prediction
# This is in comparison to making predictions built off of prior PREDICTIONS
stock[['close', 'forecast']].plot(figsize=(12, 8)) 
plt.show()