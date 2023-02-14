filename = 'Input.txt'
grades = dict()

def printStudents():
    print('-' * 27 + '\n| {0:15s} | {1:5s} |'.format('Name', 'Grade') + '\n' + '-' * 27)
    for name in grades:
        print('| {0:15s} | {1:5d} |'.format(name, grades[name]))
        print('-' * 27)

def deleteStudent(name):
    del grades[name]

def updateGrades(name, grade):
    grades[name] = grade

def searchStudent(name):
    return grades[name]

def printStats():
    temp = list(grades.keys())
    minName, maxName, total = temp[0], temp[0], 0
    for name in grades:
        if grades[minName] > grades[name]: minName = name
        if grades[maxName] < grades[name]: maxName = name
        total += grades[name]
        average = total/len(grades.keys())
        print('{} got least marks ({})'.format(minName, grades[minName]))
        print('{} got highest marks ({})'.format(maxName, grades[maxName]))
        print('Average marks = {0:.2f}'.format(average))

def saveChanges():
    res = []
    for name in grades:
        res.append('{} {}'.format(name, grades[name]))
        fh = open(filename, 'w')
        fh.write('\n'.join(res))
        fh.close()

if __name__ == '__main__':
    handler = open(filename)
    for line in handler:
        line = line.strip().split()
        grades[line[0]] = int(line[1])
    while True:
        print('1 - Print Students 2 - Change Grade 3 - Delete Student')
        print('4 - Search Student 5 - Print Stats 6 - Save into file 7 - Quit')
        option = int(input('Enter your option : '))
        if option == 1:
            printStudents()
        elif option == 2:
            name = input('Enter name : ')
            grade = int(input('Enter grade : '))
            updateGrades(name, grade)
        elif option == 3:
            name = input('Enter name : ')
            deleteStudent(name)
        elif option == 4:
            name = input('Enter name : ')
            print('Grade = {}'.format(searchStudent(name)))
        elif option == 5:
            printStats()
        elif option == 6:
            saveChanges()
        elif option == 7:
            saveChanges()
            break
        print()