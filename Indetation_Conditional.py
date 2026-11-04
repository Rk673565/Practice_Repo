#  1. Check whether a person is eligible to vote Code

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#  2. Check whether a number is positive

num = 20

if num > 0:
    print("The number is positive.")

#  3. Check whether a number is divisible by 5

number = 15
if number % 5 == 0:
    print("The number is divisible by 5.")
else:
    print("The number is not divisible by 5.")

#  4. Check whether a student's marks are greater than or equal to 35

marks = 40
if marks >= 35:
    print("pass")

#  5. Check whether a person's salary is greater than 30,000 Code
salary = 35000
if salary > 30000:
    print("The salary is greater than 30,000")

#  6. Check whether a number is greater than 100

number = 150
if number > 100:
    print("The number is greater than 100.")

# 7. Check whether a number is even or odd

number = 7
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

num = 10

if num % 2 == 0:
    print("The number is even.")

else:
    print("The number is odd.")

#  8.Check whether a number is positive or negative

number = -5
if number > 0:
    print("The number is positive.")
else:
    print("The number is negative.")

# 9. Check whether a person is eligible to vote or not

age = 21

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# 10. Check whether a student has passed or failed

marks = 45
if marks >= 35:
    print("The student has passed.")
else:
    print("The student has failed.")

# 11. Find the greatest of two numbers
num1 = 10
num2 = 20

if num1 > num2:
    print("The greatest number is:", num1)
else:
    print("The greatest number is:", num2)

#  12. Check whether a given number is divisible by 5 or not

number = 25
if number % 5 == 0:
    print("The number is divisible by 5.")
else:
    print("The number is not divisible by 5.")

# 13. Check whether a person is eligible for a driving licence
age = 16
if age >= 18:
    print("You are eligible for a driving licence.")
else:
    print("You are not eligible for a driving licence.")

# 14. Find the greatest of three numbers

num1 = 10
num2 = 20
num3 = 15

if num1 >= num2 and num1 >= num3:
    print("The greatest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("The greatest number is:", num2)
else:
    print("The greatest number is:", num3)

#  15. Display student grades based on marks

marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# 16. Check whether a number is positive, negative, or zero

number = 5
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#  17. Display the day of the week based on a number (1 to 7)

day_number = 3
if day_number == 1:
    print("Monday")
elif day_number == 2:
    print("Tuesday")
elif day_number == 3:
    print("Wednesday")
elif day_number == 4:
    print("Thursday")
elif day_number == 5:
    print("Friday")
elif day_number == 6:
    print("Saturday")
elif day_number == 7:
    print("Sunday")
else:
    print("Invalid day number.")

# 18. Check whether a given year is a leap year
year = 2026
if (year % 4 == 0 and year % 100 != 0):
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")

#  19. Calculate electricity charges based on units consumed

units = 250
if units <= 100:
    charges = units * 2
elif units <= 200:
    charges = units * 3
else:
    charges = units * 5

# 20. Simple Calculator using if-elif-else

num1 = 10
num2 = 5
operation = "+"
if operation == "+":
    result = num1 + num2
    print("Result:", result)
elif operation == "-":
    result = num1 - num2
    print("Result:", result)
elif operation == "*":
    result = num1 * num2
    print("Result:", result)
elif operation == "/":
    result = num1 / num2
    print("Result:", result)
else:
    print("Invalid operation.")

# 21. Check whether a student is eligible for an examination

attendance = 80
marks = 50

if attendance >= 75:
    if marks >= 35:
        print("The student is eligible for the examination.")

    else:
        print("The student is not eligible for the examination due to insufficient marks.")
else:
    print("The student is not eligible for the examination due to insufficient attendance.")

# 22. Validate a username and password

username = "user123"
password = "pass456"

if username == "user123":
    if password == "pass456":
        print("Login successful.")
    else:
        print("Invalid username or password.")
else:
    print("Invalid username or password.")

#  23. Check whether a person is eligible for a bank loan

age = 21
C_Score = 710

if age >= 18:
    if C_Score >= 640:
        print("The person is eligible for a bank loan.")
    else:
        print("The person is not eligible for a bank loan due to low credit score.")
else:
    print("The person is not eligible for a bank loan due to age restrictions.")

# 24. Check whether a student passed all three subjects

Telugu = 40
Hindi = 50
English = 30

if Telugu >= 35 :
    if Hindi >= 35 :
        if English >= 35:
            print("The student has passed all three subjects.")
        else:
            print("The student has failed in English.")
    else:
        print("The student has failed in Hindi.")
else:
    print("The student has failed in Telugu.")

# 25. Check whether a person is eligible for a driving licence

age = 20
if age >= 18:
    print("The person is eligible for a driving licence.")
else:
    print("The person is not eligible for a driving licence.")

# 26. Correct the indentation errors

age = 25

if age >= 18:
    print("Eligible to vote")
# 27. Correct the indentation errors


marks = 80

if marks >= 35:
    print("Pass")
else:
    print("Fail")

# 28. Correct the indentation errors

def check_age():
    if age >= 18:
        print("Eligible")
check_age(20)
#29. Correct the indentation and predict the output

age = 20

if age >= 18:
    print("Eligible")
    print("Age validation completed")

print("Program completed")

#  30. Program using a function and nested if statements


def check_eligibility(age, marks):
    if age >= 18:
        if marks >= 35:
            print("The student is eligible for the examination.")
        else:
            print("The student is not eligible for the examination due to insufficient marks.")
    else:
        print("The student is not eligible for the examination due to age restrictions.")

check_eligibility(20, 40)

#  31  Completed 

#  32 Grade B

#  33 Possitive & Even

#  34 Adult & Thank You

#  35 Fail & Result Completed


