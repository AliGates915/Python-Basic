import numpy as np
import matplotlib.pyplot as plt


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