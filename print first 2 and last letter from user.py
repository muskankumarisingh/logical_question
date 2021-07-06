a=input("enter the name:")
b=" "
i=0
while i<len(a):
    if (len(a))>3:
        if i==0:
            b=b+a[i]
        if i==1:
            b=b+a[i]
            b=b+a[-i-1]
            b=b+a[-i]
    elif len(a)<=3:
        print(a)
        break
    i=i+1
print(b)