#Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade

#start with empty list
student = []

#loop for the number of student, name, score and added to the list
    for i in range(int(input())):
        name = input()
        score = float(input())
        student.append([name, score])

#loops through inner each list EX: student = [[alice, 65], [Betty, 90]] --> each inside bracket is a inner list. And picks score(index[1]) and finds the min
lowest = min(student[1] for student in student)
second_lowest = min(student[1] for student in student if student[1] > lowest)

#loops through each inner list like before and picks the name(studetn[0]) that is only equal to second lowest
names = [student[0] for student in student if student[1] == second_lowest]

#sorts their names in alphabetical order
names.sort()

#Loops through the sorted list and prints each name on a new line.
for name in names:
    print(name)
        
        
