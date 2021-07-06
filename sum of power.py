a=int(input("enter the power"))
b=int(input("enter the number"))
add=b**a
x=str(add)
print(x)
i=0
sum=0
while i<len(x):
    sum=sum+(int(x[i]))
    i=i+1
print(sum)