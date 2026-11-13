# 1. Employee Salary Processing

employees = [
    {"name": "Rahul", "salary": 35000},
    {"name": "Anil", "salary": 50000},
    {"name": "Kiran", "salary": 45000},
    {"name": "Arun", "salary": 30000}
]

total_salary = 0
above_40000 = []

for employee in employees:

    total_salary += employee["salary"]

    if employee["salary"] > 40000:
        above_40000.append(employee["name"])

average_salary = total_salary / len(employees)

print("Total Salary =", total_salary)
print("Average Salary =", int(average_salary))
print("Employees Above 40000 =", above_40000)

