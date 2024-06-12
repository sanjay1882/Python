from abc import ABC,abstractmethod
class Veg(ABC):
 color=""
 taste=""
 def __init__(self,color,taste):
  self.color = color;
  self.taste = taste
 @abstractmethod
 def getColor(self):
  pass
 @abstractmethod
 def getTaste(self):
  pass
  
class Carrot(Veg):
 def getColor(self):
  print('Color: ',self.color)
 def getTaste(self):
  print('Taste:',self.taste)
  
  
ca = Carrot('Red','Sweet')
ca.getColor()
ca.getTaste() 
 