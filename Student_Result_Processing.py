#  Student Result Processing

def student_result(marks):

    total = 0
    highest = marks[0]
    count = 0

    for mark in marks:

        total += mark

        if mark > highest:
            highest = mark

        if mark > 75:
            count += 1

    average = total / len(marks)

    print("Total Marks =", total)
    print("Average Marks =", round(average, 2))
    print("Highest Marks =", highest)
    print("Students Above 75 =", count)


marks = [85, 60, 90, 45, 78, 55, 95]

student_result(marks)