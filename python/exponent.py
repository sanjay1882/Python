n=int(input("enter a number:"))
s=int(input("enter a exponent"))

result=1
while s !=0:
    result=result*n
    s=s-1
print("answer is "+str(result))
