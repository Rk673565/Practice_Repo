#  Employee Attendance Processing

day_1 = {101, 102, 103, 104, 105}

day_2 = {103, 104, 105, 106, 107}

present_both = day_1.intersection(day_2)

absent_second = day_1.difference(day_2)

attended_one_day = day_1.union(day_2)

print("Present Both Days =", present_both)

print("Absent On Second Day =", absent_second)

print("Attended At Least One Day =", attended_one_day)