import numpy as np
import matplotlib.pyplot as plt

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
