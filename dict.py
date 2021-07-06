dict={"1":"muskan","2":"muskan","3":"misti","4":"misti","5":"anil"}
list=[]
for val in dict.values():
    if val in list:
        continue
    else:
        list.append(val)
print(list)
