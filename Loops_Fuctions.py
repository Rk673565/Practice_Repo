#  1. Print numbers from 1 to 10

for i in range(1, 11):
    print(i)

#  2. Print even numbers between 1 and 20
for i in range(2, 21, 2):
    print(i)

#  3. Print odd numbers between 1 and 20
for i in range(1, 21, 2):
    print(i)

#  4. Calculate sum of numbers from 1 to 10

total_sum = 0
for i in range(1, 11):
    total_sum += i
print("Sum of numbers from 1 to 10:", total_sum)

# 5. Multiplication table

number = 5
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# 6. Calculate total salary

salaries = [25000, 30000, 45000, 50000, 60000]

for salary in salaries:
    print(f"Salary: {salary}")

print (sum(salaries))

#  7. Count numbers greater than 50

numbers = [10, 55, 30, 75, 90, 45, 60]
count = 0
for number in numbers:
    if number > 50:
        count += 1
print("Count of numbers greater than 50:", count)

# 8. Extract names starting with A
names = ["Anil", "Rahul", "Arun", "Kiran", "Ajay"]
x=[]
for name in names:
    if name.startswith("A"):
        x.append(name)
print("Names starting with A:", x)

#  9. Find largest number without using max()

numbers = [10, 55, 30, 75, 90, 45, 60]
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
print("Largest number:", largest)

#  10. Calculate total and average daily sales

sales = [1200, 2500, 1800, 3000, 4000]

total_sales = 0
for sale in sales:
    total_sales += sale
average_sales = total_sales / len(sales)
print("Total sales:", total_sales)
print("Average sales:", average_sales)

# 11. Function to add two numbers

def add_numbers(a, b):
    return a + b
result = add_numbers(5, 10)
print("Sum:", result)

#  12. Employee welcome message

def welcome(employee_name):
    print(f"Welcome, {employee_name}")
welcome("Sidharth")

#  13. Check even or odd

def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
check_even_odd(10)
check_even_odd(15)

# 14. Calculate square of a number

def calculate_square(number):
    return number ** 2
result = calculate_square(5)
print("Square:", result)

#  15. Function to return list length

def list_length(lst):
    return len(lst) 
lst = [1, 2, 3, 4, 5]


#  16. Find highest employee salary

def find_highest_salary(salaries):
    highest = salaries[0]
    for salary in salaries:
        if salary > highest:
            highest = salary
    return highest

salaries = [25000, 30000, 45000, 50000, 60000]
print("Highest salary:", find_highest_salary(salaries))

#  17. Calculate annual salary

def calculate_annual_salary(monthly_salary):
    return monthly_salary * 12

monthly_salary = 5000
annual_salary = calculate_annual_salary(monthly_salary)
print("Annual salary:", annual_salary)

#  18. Count vowels in a string

def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

text = "Hello, how are you?"
print("Number of vowels:", count_vowels(text))

#  19. Sum of even numbers in a list

def sum_even_numbers(numbers):
    total = 0
    for n in numbers:
        if n % 2 == 0:
            total += n
    return total

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Sum of even numbers:", sum_even_numbers(numbers))

# 20. Employees earning more than 40,000

def employees_above_threshold(salaries, threshold):
    above_threshold = []
    for salary in salaries:
        if salary > threshold:
            above_threshold.append(salary)
    return above_threshold

salaries = [25000, 30000, 45000, 50000, 60000]
threshold = 40000
employees = employees_above_threshold(salaries, threshold)
print("Employees earning more than 40,000:", employees)

# 21. Print employee names using for loop

employee_names = ["Alice", "Bob", "Charlie", "David", "Eve"]

for name in employee_names:
    print(name)

#  22. Add five new employee names 
emplyoee = ["ravali" , "priya"]
new_employees = ["sneha", "kiran", "anil", "rahul", "arun"]
for new_employee in new_employees:
    emplyoee.append(new_employee)

print("Updated employee names:")
for name in emplyoee:
    print(name)

# 23. Remove Rahul from the list

employees = ["Rahul", "Anil", "Kiran", "Arun"]
employees.remove("Rahul")
print("Updated employee names:")
for name in employees:
    print(name)

#  24. Count elements without using len()

def count_elements(lst):
    count = 0
    for _ in lst:
        count += 1
    return count

#  25. Perform set operations

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union = set1 | set2
present_day = set1 & set2
absent_day = set1 - set2

print(union)
print(present_day)
print(absent_day)

#  25. Count how many times number 10 appears

numbers = [10, 20, 10, 30, 10, 40, 50]
count = 0

for num in numbers:
    if num == 10 :
        count += 1

print("10 appears " , count ,"times")

#  26. Find the second-largest number

numbers = [10, 50, 30, 80, 60, 90]
x = []
for number in numbers:
    if number not in x :
        x.append(number) 
x.sort()
second_larg = x[-2]
print(second_larg)

#  Q27. Remove duplicate elements

numbers = [10, 20, 10, 30, 20, 40, 50]

y = []

for num in numbers :
    if num not in y:
        y.append(num)
print(y)

#  28. Reverse list without reverse() or slicing

numbers = [10, 20, 30, 40, 50]

result = []

for i in range(len(numbers) - 1, -1, -1):
    result.append(numbers[i])

print(result)

#  29. Separate positive and negative numbers

numbers = [10, -20, 30, -40, 50, -60]

positive = []
negative = []

for number in numbers:
    if number > 0:
        positive.append(number)

    elif number < 0:
        negative.append(number)

print("Positive Numbers =", positive)
print("Negative Numbers =", negative)

# 30. Calculate total, maximum and minimum prices

prices = [250, 500, 120, 800, 450, 300]

total = 0
maximum = prices[0]
minimum = prices[0]

for price in prices:
    total += price

    if price > maximum:
        maximum = price

    if price < minimum:
        minimum = price

print("Total Price =", total)
print("Maximum Price =", maximum)
print("Minimum Price =", minimum)

# 31. Create tuple and print employee names

employees = ("Rahul", "Anil", "Kiran", "Arun", "Venkat")

for employee in employees:
    print(employee)

#  32. Find total elements in tuple

numbers = (10, 20, 30, 40, 50)

count = len(numbers)

print("Total Elements =", count)

#  33. Count how many times 100 appears

numbers = (100, 200, 100, 300, 100, 400)

count = numbers.count(100)

print("100 appears", count, "times")

#  34. Find index position of Venkat

employees = ("Rahul", "Anil", "Kiran", "Venkat", "Arun")

position = employees.index("Venkat")

print("Index Position =", position)

# 35. Convert list into tuple

numbers = [10, 20, 30, 40, 50]

result = tuple(numbers)

print(result)

#  36. Convert tuple to list, add element and convert back

numbers = (10, 20, 30, 40)

new_element = 50

result = list(numbers)

result.append(new_element)

final_result = tuple(result)

print(final_result)

#  37. Find maximum and minimum without max() and min()
numbers = (45, 12, 89, 34, 100, 67)

maximum = numbers[0]
minimum = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number

    if number < minimum:
        minimum = number

print("Maximum =", maximum)
print("Minimum =", minimum)

#  38. Employee tuple unpacking
employee = (101, "Venkat", 50000)

employee_id, employee_name, salary = employee

print("Employee ID =", employee_id)
print("Employee Name =", employee_name)
print("Salary =", salary)

#  39. Calculate average daily temperature

temperatures = (30, 32, 31, 29, 35, 33)

total = 0
count = 0

for temperature in temperatures:
    total += temperature
    count += 1

average = total / count

print("Average Temperature =", round(average, 2))


#  40. Count students scoring above 75

marks = (85, 60, 90, 45, 78, 55, 95)

count = 0

for mark in marks:
    if mark > 75:
        count += 1

print("Students Scoring Above 75 =", count)

#  41. Create set and print all elements
numbers = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}

for number in sorted(numbers):
    print(number)

#  42. Add five new elements to existing set

numbers = {10, 20, 30}

new_numbers = {40, 50, 60, 70, 80}

numbers.update(new_numbers)

print(numbers)

#  43. Remove number 50 from set

numbers = {10, 20, 30, 40, 50, 60}

numbers.discard(50)

print(numbers)

#  44. Find unique elements using set
numbers = [10, 20, 10, 30, 20, 40, 50, 10]

unique_numbers = set(numbers)

print("Unique Elements =", unique_numbers)

print("Unique Count =", len(unique_numbers))

#  45 45. Find union of two sets

set1 = {10, 20, 30, 40}

set2 = {30, 40, 50, 60}

result = set1.union(set2)

print("Union =", result)

#  46. Find common employee IDs using intersection

set1 = {101, 102, 103, 104}

set2 = {103, 104, 105, 106}

result = set1.intersection(set2)

print("Common Employee IDs =", result)

#  47. Find difference between two sets

set1 = {10, 20, 30, 40, 50}

set2 = {30, 40, 60, 70}

result = set1.difference(set2)

print("Difference =", result)

#  48. Find unique customer IDs from two branches

branch_1 = [101, 102, 103, 104, 105]

branch_2 = [103, 104, 106, 107, 108]

all_customers = set(branch_1).union(set(branch_2))

print("Unique Customer IDs =", all_customers)

print("Total Unique Customers =", len(all_customers))

#  49. Employees attended training in both months

january = {101, 102, 103, 104}

february = {103, 104, 105, 106}

result = january.intersection(february)

print("Employees Attended Both Months =", result)

#  50. Identify duplicate customer emails

emails_1 = ["a@gmail.com", "b@gmail.com", "c@gmail.com"]

emails_2 = ["b@gmail.com", "d@gmail.com", "a@gmail.com"]

duplicates = set(emails_1).intersection(set(emails_2))

print("Duplicate Emails =", duplicates)

