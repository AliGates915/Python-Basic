import numpy as np
import matplotlib.pyplot as plt

# 1. Temperature Data
temps = np.array([22, 24, 19, 25, 28, 21, 26, 30, 27, 24, 
                  23, 25, 29, 31, 28, 26, 22, 24, 25, 29, 
                  30, 27, 26, 25, 24, 23, 22, 26, 27, 28])

# 2. Basic Analysis
avg_temp = np.mean(temps)
max_temp = np.max(temps)
min_temp = np.min(temps)

print(f"Average Temperature: {avg_temp:.2f}°C")
print(f"Maximum Temperature: {max_temp}°C")
print(f"Minimum Temperature: {min_temp}°C")

# 3. Days hotter than average
hotter_days = np.where(temps > avg_temp)[0] + 1  # +1 to make days start from 1
print(f"Days hotter than average: {hotter_days}")

# 4. Plotting
days = np.arange(1, 31)

plt.figure(figsize=(10, 5))
plt.plot(days, temps, marker='o', linestyle='-', color='blue', label='Temperature')
plt.axhline(y=avg_temp, color='red', linestyle='--', label=f'Avg Temp ({avg_temp:.2f}°C)')
plt.title("Temperature Trend for the Month")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.show()
