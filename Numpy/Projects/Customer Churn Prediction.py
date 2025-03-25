import numpy as np
import matplotlib.pyplot as plt

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