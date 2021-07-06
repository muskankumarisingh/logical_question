a=[2,2.5,"9"]
a1=[]
sum=0
i=0
while i<len(a):
    if a[i] not in a1:
        a[i]=int(a[i])
        sum=sum+a[i]
        a1.append(sum)
    i=i+1
print(sum)