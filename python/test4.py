from abc import ABC,abstractmethod
class Test (ABC):
 def display(self,name):
  print("name=",name)
  
 @abstractmethod
 def printname (self,name):
  pass
  
class Test1:
 def dis(self,name):
  print("dis=",name)
class chlid(Test):
 pass
 c.child()
 c= print x()
