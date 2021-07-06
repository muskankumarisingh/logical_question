dic={}
while True:
    name=input("enter the employee name :")
    num=int(input("enter the employee salary :"))
    dic[name]=num
    user=input("do you want to quit then enter yes \ no :")
    if user=="yes":
        break
print(dic)
