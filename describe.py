import pandas as pd

data = {
    "Name": ['Ram', 'Shyam', 'Ghnashyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age": [28, 34, 22, 30, 29, 40, 25, 32],
    "Salary": [50000, 60000, 55000, 70000, 72000, 80000, 65000, 62000,],
    "Performance Score": [85, 90, 78, 88, 92, 95, 80, 84]
}

df = pd.DataFrame(data)
print("DataFrame:")
print(df)
print("\nDescriptive Statistics:")
print(df.describe())