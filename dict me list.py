num=[{"name":"muskan","age":21},{"name":"tanjum","age":22},{"name":"srishti","age":23},{"name":"mamatha","age":22}]
var=input("enter the name")
age=int(input("enter the age"))
i=0
while i<len(num):
    b=[]
    j=0
    for j in num:
        if var==j["name"]:
             b.append(j)
    i=i+1
print(b)
k=0
while k<len(num):
    c=[]
    for x in num:
        if age==x["age"]:
            c.append(x)
    k=k+1
print(c)
z=[]
for l in num:
    if l["age"]>=20:
        z.append(l)
print(z)






