#Task 1 Given the list of grades

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
#sort in descending order
grades.sort()
grades.reverse()
print(grades)

#Task 2 - Find the average
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
count = len(grades)
avg_grades = sum(grades) / count
print(avg_grades)