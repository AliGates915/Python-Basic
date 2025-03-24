import numpy as np
import matplotlib.pyplot as plt
# You have data for monthly marketing spend and sales revenue. The task is to:
# Analyze the relationship. 
# Plot trends.
# Discuss correlation.
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
marketing_spend = [3000, 3500, 4000, 4500, 5000, 5500]
sales = [5000, 5200, 6100, 6700, 7100, 7800]

# Correlation
corr = np.corrcoef(marketing_spend, sales)[0,1]
print(f"Correlation between marketing spend and sales: {corr:.2f}")

plt.plot(months, marketing_spend, label='Marketing Spend', marker='o')
plt.plot(months, sales, label='Sales', marker='s')
plt.legend()
plt.title("Marketing Spend vs Sales")
plt.xlabel("Months")
plt.ylabel("Amount ($)")
plt.tight_layout()
plt.show()