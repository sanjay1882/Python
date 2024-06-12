from Student import Student
studentList = []
while True:
 print('1. Add','2. Remove','3. Display All','4. Exit',sep='\n')
 a=int(input("Enter option: "))
 if a==4:
  break
 elif a==1:
  b=input("Enter a name: ")
  c=input("enter a valid email id: ")
  d=input("Enter your date of birth(dd/MM/YYYY):")
  e=input("enter a mobile number: ")
  isAdd=True
  for student in studentList:
   if student.email == c :
    student.display()
    print('Email Id already exists')
    isAdd=False
    break
  if isAdd :    
   x=Student(b,c,d,e )
   x.display()
   studentList.append(x)
 elif a==2:
  email=input("enter a valid email id: ")
  for student in studentList:
   if student.email == email :
    student.display()
    studentList.remove(student)
    break  
 elif a==3:
  for stu in studentList:
   stu.display()
 
  
  





