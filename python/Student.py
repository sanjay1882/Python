class Student:
 name=''
 email=''
 dob=''
 mobile=''
 def __init__(self,name,email,dob,mobile):
  self.name=name
  self.email=email
  self.dob=dob
  self.mobile=mobile
  
 def display(self):
  print('------------------------')
  print('Name: ',self.name,sep='')
  print('Email: ',self.email,sep='')
  print('dob: ',self.dob,sep='')
  print('mobile :',self.mobile,sep='')
  print('*************************')
  

 
  

 