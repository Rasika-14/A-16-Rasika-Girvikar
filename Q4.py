Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Student(object):
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks
    
    def getmarks(self):
        return self.marks
    
    def getroll(self):
        return self.roll
    
    def __str__(self):
        return self.name + ' : ' + str(self.getroll()) +'  ::'+  str(self.getmarks())

>>> def Markss(rec, name, roll, marks):
    rec.append(Student(name, roll, marks))
    return rec

>>> Record = []
>>> x = 'y'
>>> while x == 'y':
    name = input('Enter the name of the student: ')
    height = input('Enter the roll number: ')
    roll = input('Marks: ')
    Record = Markss(Record, name, roll, height)
    x = input('another student? y/n: ')

Enter the name of the student: Rasika
Enter the roll number: 1
Marks: 90
another student? y/n: y
Enter the name of the student: Ketaki
Enter the roll number: 2
Marks: 92
another student? y/n: y
Enter the name of the student: Ram
Enter the roll number: 3
Marks: 78
another student? y/n: y
Enter the name of the student: Sham
Enter the roll number: 4
Marks: 76
another student? y/n: y
Enter the name of the student: Amol
Enter the roll number: 5
Marks: 88
another student? y/n: n
>>> n = 1
>>> for el in Record:
    print(n,'. ', el)
    n = n + 1

    
1 .  Rasika : 90  ::1
2 .  Ketaki : 92  ::2
3 .  Ram : 78  ::3
4 .  Sham : 76  ::4
5 .  Amol : 88  ::5
>>> 