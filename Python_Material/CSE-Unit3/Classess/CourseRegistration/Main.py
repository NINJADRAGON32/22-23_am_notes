
    #from FileName import Class
from Teacher import Teacher
from studentClass import Student
from Course import Course
import random  #built in module, no need for the from syntax

masterTeacherList = []
masterStudentList = []
masterCourseList = []
#read from DB

def loadStudent():
    file1 = open("StudentDatabase.txt","r")
    f = file1.readlines()
    for line in f:
        #print the line and strip everything to the right
        first,last = line.rstrip().split(",")
        #create new student object
        newStudent = Student(first,last)
        #add student to masterStudentList
        masterStudentList.append(newStudent)
        
def printStudents():
    #print out each student and their courses          
    for student in masterStudentList:
        print(student)

def loadCourse():
    #read csv file
    file1 = open("CourseCatalog.csv","r")
    f = file1.readlines()
    for line in f:
        #print the line and strip everything to the right
        id,name,description = line.rstrip().split(",")
         #create course object
        newCourse = Course(id,name)
        #save course object
        masterCourseList.append(newCourse)
        
def assignCourses():
    #randomly add courses to students
    for student in masterStudentList:
        listOfCourses=masterCourseList.copy()
        #loop 4 times because we have 4 class to add
        for i in range(4):       #never use the i
            courseToAdd = listOfCourses.pop(random.randrange(0,len(listOfCourses)))
            student.addCourse(courseToAdd)
    for teacher in masterTeacherList:
        listOfCourses=masterCourseList

def printOutSchedules():
    #creates a new file for each student to print out for first day schedule
    for student in masterStudentList:
        fileToriteTo = open(f"{student.lastName}_{student.firstName}.txt","w")
        fileToriteTo.write(student.__str__())
        fileToriteTo.close()

def loadTeacher():
    file1 = open("TeacherDatabase.txt","r")
    f = file1.readlines()
    for line in f:
        #print the line and strip everything to the right
        first,last = line.rstrip().split(",")
        #create new student object
        newStudent = Student(first,last)
        #add student to masterStudentList
        masterStudentList.append(newStudent)
    
def printTeacher():
    #print out each student and their courses          
    for teacher in masterTeacherList:
        print(teacher)
#run the functions
loadStudent()
loadCourse()
assignCourses()
printStudents()
printOutSchedules()
loadTeacher()
printTeacher()





