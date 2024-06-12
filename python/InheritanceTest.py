class person:
 def __init__(self,fname,lname):
  self.firstname = fname
  self.lastname = lname
 def printname(self):
  print(self.firstname, self.lastname)

#Child class 
class Student(Person):
 def printchild(self):
   print("Child ",self.firstname, self.lastname)
  
class Teacher(Person):
 def printchild(self):
   print("Child Teacher ",self.firstname, self.lastname)
 
x = Person("John","Doe")
x.printname()

s = Student("MK","SK")
s.printname()
s.printchild()

s = Teacher("GH","RH")
s.printname()
s.printchild()