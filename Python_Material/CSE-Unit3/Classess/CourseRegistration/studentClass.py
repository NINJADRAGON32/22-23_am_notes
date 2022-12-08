#classes bellringer for student classes

class Student:
    
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName=lastName
        self.courses=[]
        
    def __str__(self):
        out = f"{self.lastName} , {self.firstName}\n"
        for c in self.courses:
            out += f"\t{c}\n"
        return out
    
    def getFirstName(self):
        return self.firstName
    
    def getLastName(self):
        return self.lastName
    
    def addCourse(self,newCourse):
        self.courses.append(newCourse)
        
    