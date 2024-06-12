class TestClass:
 c = 0;
 def add(self,x,y):
  print(x+y)
 def sub(self,x,y):
  print(x-y)
 def mul(self,x,y):
  print(x*y)
 def div(self,x,y):
  print(x/y)
 def ab2(self,x,y):
  print((x*x)+(2*x*y)+(y*y))
  print('c=',self.c)
 
myClass = TestClass() #Object Creation
print('c--before ---',myClass.c) #Access global variable by object                                                                                                                                                                                                                                                                                                                                   \/

g=int(input('Enter number1'))
h=int(input('Enter number2'))
myClass.add(g,h)
myClass.sub(g,h)
myClass.sub(8,5)
myClass.ab2(g,h) 
  


