
    #from FileName import Class
from studentClass import Student
from Course import Course
import random  #built in module, no need for the from syntax


masterStudentList = []
masterCourseList = []
#read from DB


def loadStudent(firstName,lastName):
    file1 = open("StudentDatabase.txt","r")
    f = file1.readlines()
    for line in f:
        #print the line and strip everything to the right
        first,last = line.rstrip().split(",")
        #create new student object
        newStudent = Student(firstName, lastName)
        #add student to masterStudentList
        masterStudentList.append(newStudent)
        
    
    #randomly add courses to students
    for student in masterStudentList:
        listOfCourses=masterCourseList.copy()
        #loop 4 times because we have 4 class to add
        for i in range(4):       #never use the i

            courseToAdd = listOfCourses.pop(random.randrange(0,len(listOfCourses)))
            student.addCourse(courseToAdd)
            
        #watch out to not duplicate a course in the schedule
          
    
        #print out each student and their courses
    for student in masterStudentList:
        print(student)

def loadCourse():
    #read csv file
    #create course object
    #save course object
    pass #placeholder to tell python to keep moving








