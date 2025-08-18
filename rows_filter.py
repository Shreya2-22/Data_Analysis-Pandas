import pandas as pd

data = {
    "Name": ['Ram', 'Shyam', 'Ghnashyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age": [28, 34, 22, 30, 29, 40, 25, 32],
    "Salary": [50000, 60000, 55000, 70000, 72000, 80000, 65000, 62000,],
    "Performance Score": [85, 90, 78, 88, 92, 95, 80, 84]
}
df = pd.DataFrame(data)
print(df)

high_salary = df[df["Salary"] > 50000]
print("\nHigh Salary Employees:")
print(high_salary)

#filtering rows salary>50k & age>30
filtered = df[(df["Salary"] > 50000) & (df["Age"] > 30)]
print("\nFiltered Employees (Salary > 50k & Age > 30):")
print(filtered)