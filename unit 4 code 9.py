import numpy as np
import pandas as pd

# 1. Create a NumPy array of course fees
# (Sample courses data used to construct the DataFrame later)
courses = np.array(["Data Science", "Web Development", "AI & ML", "Cybersecurity", "Cloud Computing"])
fees = np.array([30000, 18000, 45000, 22000, 28000])

# 2. Calculate average, maximum, and minimum course fee
avg_fee = np.mean(fees)
max_fee = np.max(fees)
min_fee = np.min(fees)

print("--- Fee Statistics ---")
print(f"Average Fee: ₹{avg_fee:,.2f}")
print(f"Maximum Fee: ₹{max_fee:,}")
print(f"Minimum Fee: ₹{min_fee:,}\n")

# 3. Create a Pandas DataFrame
df = pd.DataFrame({
    'Course Name': courses,
    'Course Fee (₹)': fees
})

print("--- Complete Course DataFrame ---")
print(df, "\n")

# 4. Display courses whose fee is greater than ₹25,000
high_fee_courses = df[df['Course Fee (₹)'] > 25000]

print("--- Courses with Fees Greater than ₹25,000 ---")
print(high_fee_courses)
