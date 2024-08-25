class Student:
    def __init__(self, id, name, mathScore, litScore, chemScore):
        self.id = id
        self.name = name
        self.mathScore = mathScore
        self.litScore = litScore
        self.chemScore = chemScore
    
    def avgScore(self):
        return round((self.mathScore + self.litScore + self.chemScore) / 3, 2)



def main():
    studentList = []

    while True:
        option = input("Add new student? Enter Yes or No: ")
        if option.lower() == 'y':
            id = input('Student ID: ')
            name = input('Student name: ')
            mathScore = int(input('Student math score: '))
            litScore = int(input('Student literature score: '))
            chemScore = int(input('Student chemistry score: '))

            newStudent = Student(id, name, mathScore, litScore, chemScore)
            studentList.append(newStudent)
        elif option.lower() == 'n':
            break
        else:
            print('Invalid command.')

    print(f'Number of student: {len(studentList)}')

    print('List of students with average score higher than 5: ')
    count = 1
    for i, student in enumerate(studentList):
        if student.avgScore() > 5:
            print(f'Student #{count}: ', end='')
            print(dict(id=student.id, name=student.name, math=student.mathScore, literature = student.litScore, chemistry = student.chemScore))
            count += 1

    
    print('List of stundents with chemistry score lower than 5: ', end='')
    chemList = []
    for i in studentList:
        if i.chemScore < 5:
            chemList.append(i.name)
    print(', '.join(chemList))

if __name__ == '__main__':
    main()