# a="i like banana i like banana i like banana i like banana"
# a=a.replace("banana","mango")
# print(a)

# without replace using
a="i like banana i like banana i like banana i like banana"
a=a.split()
new=""
i=0
while i<len(a):
    if a[i]=="banana":
        new=new+"mango"+" "
    else:
        new=new+a[i]+" "
    i=i+1
print(new)

