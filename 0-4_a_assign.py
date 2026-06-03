import pandas as pd

# Load CSV
df = pd.read_csv("employee.csv")

print("===== EMPLOYEE DATA =====")
print(df)

# Average Salary
avg_salary = df["Salary"].mean()

print("\nAverage Salary:")
print(avg_salary)

# Department Count
dept_count = df["Department"].value_counts()

print("\nDepartment Count:")
print(dept_count)

# Filter Employees Above Threshold
threshold = 60000

high_salary = df[df["Salary"] > threshold]

print("\nEmployees with Salary Above", threshold)
print(high_salary)

# Export Result to New CSV
high_salary.to_csv("high_salary_employees.csv", index=False)

print("\nFiltered data exported successfully!")