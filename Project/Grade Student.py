# Name: Hoang Long Nguyen
# Class: CS 1314
# Project: Table Grade

filename = 'Grade'
grades = dict()


# Print table
def printstudents():
    print('-' * 32 + "\n| {0:15s} | {1:5s}|".format('Name', 'Total Grade ') + '\n' + '-' * 32)
    for nameStudent in grades:
        print('| {0:15s} |   {1:.2f}  |'.format(nameStudent, grades[nameStudent]))

    print('-' * 32)


# Delete a student
def deletestudent(namestudent):
    del grades[namestudent]


# Update Grade of student
def gradesofstudent(namestudent, gradestudent):
    grades[namestudent] = gradestudent


# Search for grade of a student
def searchstudent(namestudent):
    return grades[namestudent]


# Print average of all Student
def printstatistic():
    temp = list(grades.keys())
    minname = temp[0]
    maxname = temp[0]
    total = 0
    for nameStudent in grades:
        if grades[minname] > grades[nameStudent]:
            minname = nameStudent
        if grades[maxname] < grades[nameStudent]:
            maxname = nameStudent
        total += grades[nameStudent]
    average = total / len(grades.keys())
    print('{} got least marks: {}'.format(minname, grades[minname]))
    print('{} got highest marks: {}'.format(maxname, grades[maxname]))
    print('Average marks = {0:.2f}'.format(average))


# Save data changes to the file
def savechanges():
    res = []
    for nameStudent in grades:
        res.append('{} {}'.format(nameStudent, grades[nameStudent]))
    fh = open(filename, 'w')
    fh.write("\n".join(res))
    fh.close()


# Show all choice for Professor to choose and read file
if __name__ == '__main__':
    handler = open(filename)
    for line in handler:
        line = line.strip().split()
        grades[line[0]] = float(line[1])
    while True:
        print('1. Print Table Grade of Students ')
        print('2. Change Grade and Add Student & Grade ')
        print('3. Delete Student')
        print('4. Search Student ')
        print('5. Print Statistic ')
        print('6. Save into file ')
        print('7. Quit')
        option = int(input("Enter your option: "))
        if option == 1:
            printstudents()
        elif option == 2:
            name = input("Enter name: ")
            grade = float(input('Enter grade: '))
            gradesofstudent(name, grade)
        elif option == 3:
            name = input("Enter name: ")
            deletestudent(name)
        elif option == 4:
            name = input("Enter name: ")
            print('Grade = {}'.format(searchstudent(name)))
        elif option == 5:
            printstatistic()
        elif option == 6:
            savechanges()
        elif option == 7:
            savechanges()
            break
        print()
