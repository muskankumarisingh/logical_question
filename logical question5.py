def my_function():
    dic={}
    name=input("enter the name")
    age=int(input("enter the age"))
    roll_no=int(input("enter the roll_no"))
    a=name
    b=age
    c=roll_no
    for i in range(3):
        dic["name"]=a
        dic["age"]=b
        dic["roll_no"]=c
    print(dic)
my_function()


# stud_data={}

# for i in stud_data:
#     Name = input("enter name")
#     Age = int(input("enter num"))
#     Grade = int(input("enter num"))
#     Nam_key =  Name[0]
#     Age_value = Age[0]
#     Grade_value = Grade[0]
#     stud_data[Nam_key] = Age_value
#     stud_data[Nam_key]=Grade_value
#     print(stud_data)