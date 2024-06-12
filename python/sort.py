class Testsort:
 c=[]
 def __init__ (self,a):
  self.c=a
 def sort(self):
  for i in range(0,len(self.c)):
   for j in range(i+1,len(self.c)):
    if self.c[i] > self.c[j]:
     x=self.c[i]
     self.c[i]=self.c[j]
     self.c[j]=x
  return self.c

l=[1,4,2,3]
d=Testsort(l)
print(d.sort())

 