import numpy as np
import matplotlib.pyplot as plt

# Simulate monthly sales data for a shop (in USD)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# we get the same random values every time for consistency.
np.random.seed(0)  
sales = np.random.randint(1000, 5000, size=12)
# Example sales => [4840, 3592, 4069, 4914, 4949, 2533, 4055, 4561, 2675, 4262, 4842, 1139]


# Calculate total and average sales
total_sales = np.sum(sales)
average_sales = np.mean(sales)

# The zip() function combines two (or more) lists together into pairs (or tuples), so you can loop over them at the same time.

print("Monthly Sales Data (USD):")
for month, sale in zip(months, sales):
    print(f"{month}: ${sale}")

print(f"\nTotal Sales for the year: ${total_sales}")
print(f"Average Monthly Sales: ${average_sales:.2f}")

# Plotting the sales data
plt.figure(figsize=(10,5))
plt.plot(months, sales, marker='o', linestyle='-', color='blue', label='Monthly Sales')
plt.axhline(average_sales, color='red', linestyle='--', label='Average Sales')
plt.title('Monthly Sales Report')
plt.xlabel('Months')
plt.ylabel('Sales (USD)')
plt.legend() # will display a small box on the graph with these labels.
plt.grid(True)
plt.tight_layout() 
# tight_layout is used to automatically adjust the spacing between subplots and other elements (like axis labels, title, and legend) to prevent them from overlapping.
plt.show()
