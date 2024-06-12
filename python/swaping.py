a=int(input("enter a number"))
b=int(input("enter a number:"))
#To swap the variable of two numbers
a,b=b,a
print("the value a swapping:",a)
print("the value b swapping:",b)


#solution2
a=int(input("enter a number"))
b=int(input("enter a number:"))

temp=a
a=b
b=temp
print(a)
print(b)


#solution3
a=int(input("enter a number"))
b=int(input("enter a number:"))
a=a+b
b=a-b 
a=a-b
print(a)
print(b)