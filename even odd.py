list=[1,2,3,4,5,6,7,8,9,10]
i=0
while i<len(list):
    if list[i]%2==0:
        print(list[i],"even")
    else:
        print(list[i],"odd")
    i=i+1