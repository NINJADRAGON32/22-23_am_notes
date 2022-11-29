class Teacher:
    
    def __init__(self,firstName,lastName,subject):
        self.firstName = firstName
        self.lastName=lastName
        self.subject=subject
        self.courses=[]
        
    def __str__(self):
        out = f"{self.lastName} - {self.subject}\n"
        out += f"\tperiod 1 :{self.subject}\n \tperiod 2 :{self.subject}\n \tperiod 3 :{self.subject}\n"
        return out
    
    def getFirstName(self):
        return self.firstName
    
    def getLastName(self):
        return self.lastName
    
    def addCourse(self,newCourse):
        self.courses.append(newCourse)