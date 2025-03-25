import numpy as np
import matplotlib.pyplot as plt
# Analyze the closing prices of a stock (e.g., Amazon) over 30 days:
# Plot moving average.
# Highlight buy/sell signals.
# Mark max/min prices.

days = np.arange(1, 31)
closing_prices = np.random.randint(100, 200, size=30)

# Moving average (window=5)
moving_avg = np.convolve(closing_prices, np.ones(5)/5, mode='valid')

plt.plot(days, closing_prices, label='Closing Price', marker='o', ) # by default color assign light blue. color = 'lightblue'
plt.plot(days[4:], moving_avg, label='5-Day Moving Avg', linestyle='--') # by default color assign orange color = 'orange'
plt.scatter(days[np.argmax(closing_prices)], max(closing_prices), color='green', label='Max Price')
plt.scatter(days[np.argmin(closing_prices)], min(closing_prices), color='red', label='Min Price')
plt.legend()
plt.title("Stock Prices with Moving Average")
plt.xlabel("Day")
plt.ylabel("Price ($)")
plt.tight_layout()
plt.show()

