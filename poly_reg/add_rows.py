import pandas as pd
import time
import random
# Read the current CSV
df = pd.read_csv('poly_reg/Position_Salaries.csv')

# Define the new rows to add
new_rows = [
    {'Position': 'Executive CEO', 'Level': 11, 'Salary': 1100000},
    {'Position': 'Global Partner', 'Level': 12, 'Salary': 1200000},
    {'Position': 'Chief Strategist', 'Level': 13, 'Salary': 1300000},
    {'Position': 'Senior Manager', 'Level': 14, 'Salary': 1400000},
    {'Position': 'Regional Director', 'Level': 15, 'Salary': 1500000},
    {'Position': 'International Consultant', 'Level': 16, 'Salary': 1600000},
    {'Position': 'Corporate Analyst', 'Level': 17, 'Salary': 1700000},
    {'Position': 'Vice President', 'Level': 18, 'Salary': 1800000},
    {'Position': 'Board Member', 'Level': 19, 'Salary': 1900000},
    {'Position': 'Founder', 'Level': 20, 'Salary': 2000000},
    {'Position': 'Co-Founder', 'Level': 21, 'Salary': 2100000},
    {'Position': 'Chief Executive', 'Level': 22, 'Salary': 2200000},
    {'Position': 'Managing Director', 'Level': 23, 'Salary': 2300000},
    {'Position': 'Operations Head', 'Level': 24, 'Salary': 2400000},
    {'Position': 'Finance Director', 'Level': 25, 'Salary': 2500000},
    {'Position': 'Marketing Lead', 'Level': 26, 'Salary': 2600000},
    {'Position': 'Tech Lead', 'Level': 27, 'Salary': 2700000},
    {'Position': 'HR Director', 'Level': 28, 'Salary': 2800000},
    {'Position': 'Sales Director', 'Level': 29, 'Salary': 2900000},
    {'Position': 'Product Manager', 'Level': 30, 'Salary': 3000000}
]

# Add rows one by one with 1 minute delay
for row in new_rows:
    new_df = pd.DataFrame([row])
    df = pd.concat([df, new_df], ignore_index=True)
    df.to_csv('poly_reg/Position_Salaries.csv', index=False)
    print(f"Added row: {row}")
    time.sleep(random.choice([10,20,15]))  # Wait 1 minute
for row in new_rows:
    new_df = pd.DataFrame([row])
    df = pd.concat([df, new_df], ignore_index=True)
    df.to_csv('poly_reg/Position_Salaries.csv', index=False)
    print(f"Added row: {row}")
    time.sleep(random.choice([10,20,15])) 
for row in new_rows:
    new_df = pd.DataFrame([row])
    df = pd.concat([df, new_df], ignore_index=True)
    df.to_csv('poly_reg/Position_Salaries.csv', index=False)
    print(f"Added row: {row}")
    time.sleep(random.choice([10,20,15])) 
for row in new_rows:
    new_df = pd.DataFrame([row])
    df = pd.concat([df, new_df], ignore_index=True)
    df.to_csv('poly_reg/Position_Salaries.csv', index=False)
    print(f"Added row: {row}")
    time.sleep(random.choice([10,20,15])) 
for row in new_rows:
    new_df = pd.DataFrame([row])
    df = pd.concat([df, new_df], ignore_index=True)
    df.to_csv('poly_reg/Position_Salaries.csv', index=False)
    print(f"Added row: {row}")
    time.sleep(random.choice([10,20,15])) 
for row in new_rows:
    new_df = pd.DataFrame([row])
    df = pd.concat([df, new_df], ignore_index=True)
    df.to_csv('poly_reg/Position_Salaries.csv', index=False)
    print(f"Added row: {row}")
    time.sleep(random.choice([10,20,15])) 
print("All rows added.")