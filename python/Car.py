class Car:
 name=''
 color=''
 def __init__(self,na,cl )
  self.name = na
  self.color = cl
 def getPrice(self):
  x=0
  print(self.name,' clolor:',self.color)
  if self.name == 'Maruthi' and self.color == 'Red' :
   x=100000
  elif self.name == 'Ford' and self.color == 'Black' :
   x=200000
  elif self.name == 'KIA' and self.color == 'White' :
   x=300000
  elif  self.name == 'Nissan' and self.color == 'Blue' :
   x=400000
  else :
   x=0
  return x
   
c = Car('Maruthi','Red')
price = c.getPrice()
print('Maruthi car price is' , price)

c = Car('Nissan','Blue')
price = c.getPrice()
print('Nissan car price is' , price)