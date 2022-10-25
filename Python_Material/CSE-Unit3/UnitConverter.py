import random
from Conversion import *
#from FileName import everything

#convert any unit to any unit...  kind of

# the 3 apostrophes are string formatting
menu='''
     in to cm (ic)
     cm to in (ci)
     kg to g  (kgg)
     g to kg  (gkg)
     
     which conversion? 
'''
user=input(menu)
#loop until the user says quit
while(user!="quit"):
     #run that specific conversion
     if user=="ic":
          #run the in to cm function
          in2cm()
     elif user=="ci":
          #run the cm to in function
          cm2in()
     elif user=="kgg":
          kg2g()
     elif user=="gkg":
          g2kg()
     
     #ask the user which conversion?
     user=input(menu)
     
#define functions above where you run them