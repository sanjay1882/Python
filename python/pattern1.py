#solution1
a=int(input("enter a number :"))
for i in range (1,a+1,1):
 for j in range(1,i+1,1):
  print('*',end='')
 print()
 
 
 #solution2
 for i in range (1,a+1,1):
  for j in range (1,i+1,1):
   if i%2==0 :
    print('-',end=' ')
   else:
    print('*',end=' ')
  print()
  
a=int(input("ENTER A NUMBER :"))
for  i in range(1,a+1):
 for j in range(1,i+1):
  print('#',end='')
 print()
 
  