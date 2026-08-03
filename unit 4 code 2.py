import numpy as np
import pandas as pd

# 1. Create a NumPy array of employee salaries
# (Using sample data for demonstration)
salaries_array = np.array([55000, 72000, 48000, 65000, 80000, 59000])
employee_names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"]

# 2. Calculate average, maximum, and minimum salary
avg_salary = np.mean(salaries_array)
max_salary = np.max(salaries_array)
min_salary = np.min(salaries_array)

print("--- Salary Statistics ---")
print(f"Average Salary: ₹{avg_salary:,.2f}")
print(f"Maximum Salary: ₹{max_salary:,.2f}")
print(f"Minimum Salary: ₹{min_salary:,.2f}\n")

# 3. Create a Pandas DataFrame
df = pd.DataFrame({"Employee Name": employee_names, "Salary": salaries_array})

print("--- Full Employee DataFrame ---")
print(df, "\n")

# 4. Display employees earning more than ₹60,000
high_earners = df[df["Salary"] > 60000]

print("--- Employees Earning More Than ₹60,000 ---")
print(high_earners.to_string(index=False))
