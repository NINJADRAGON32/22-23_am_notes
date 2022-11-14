
    #from FileName import Class
from studentClass import Student
from Course import Course
import random  #built in module, no need for the from syntax

#create a course
cs = Course("Comp Sci 1")
lunch = Course("Diners Drive-in Dives")
history = Course("American History post 1776")
gym = Course("Retirement Sports")

#create a student

masterStudentList = []
masterCourseList = [cs,lunch,history,gym]
#read from DB
file1 = open("StudentDatabase.txt","r")
f = file1.readlines()

def loadStudent(firstName,lastName):
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

for line in f:
    #print the line and strip everything to the right
    first,last = line.rstrip().split(",")
    loadStudent(first,last)





