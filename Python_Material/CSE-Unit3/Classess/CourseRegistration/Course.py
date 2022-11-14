#define class
class Course:
    
    #course(course name)
    def __init__(self,id,name):
        self.name = name
        self.id = id
        
    #toString -> courseName
    def __str__(self):
        # return self.id +
        return f"{self.id} {self.name}"
    