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

plt.plot(days, closing_prices, label='Closing Price', marker='o')
plt.plot(days[4:], moving_avg, label='5-Day Moving Avg', linestyle='--')
plt.scatter(days[np.argmax(closing_prices)], max(closing_prices), color='green', label='Max Price')
plt.scatter(days[np.argmin(closing_prices)], min(closing_prices), color='red', label='Min Price')
plt.legend()
plt.title("Stock Prices with Moving Average")
plt.xlabel("Day")
plt.ylabel("Price ($)")
plt.tight_layout()
plt.show()






#  Scenario 3: Sensor Data from IoT Devices
# ------------------------

hours = np.arange(0, 24)
temp = np.random.randint(15, 40, size=24)
humidity = np.random.randint(30, 80, size=24)

plt.scatter(temp, humidity, c='purple')
plt.title("Temperature vs Humidity")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.tight_layout()
plt.show()

# Detect anomalies (temperature > 35 or humidity > 70)
anomalies = [(t, h) for t, h in zip(temp, humidity) if t > 35 or h > 70]
print("Anomalies:", anomalies)

# ------------------------
# Scenario 4: Customer Churn Prediction (EDA part)
# ------------------------

customer_ids = ['C1', 'C2', 'C3', 'C4', 'C5']
tenure = [1, 24, 5, 36, 3]  # in months
charges = [90, 55, 85, 45, 95]  # monthly charges in $

plt.scatter(tenure, charges, c='blue')
plt.title("Tenure vs Monthly Charges")
plt.xlabel("Tenure (months)")
plt.ylabel("Charges ($)")

# Highlight churn risk customers (low tenure + high charges)
for cid, t, c in zip(customer_ids, tenure, charges):
    if t < 6 and c > 80:
        plt.annotate(cid, (t, c), color='red')

plt.tight_layout()
plt.show()

# ------------------------
# Scenario 5: Flight Delay Analysis
# ------------------------

hours = np.arange(0, 24)
delays = np.random.randint(0, 120, size=24)  # delays in minutes

plt.bar(hours, delays, color='skyblue')
plt.title("Flight Delays per Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Delay (min)")
plt.tight_layout()
plt.show()

avg_delay = np.mean(delays)
print(f"Average delay: {avg_delay:.2f} minutes")
