string="my name is muskan"
dict={}
i=0
while i<len(string):
    j=0
    count=0
    while j<len(string):
        if string[i]==string[j]:
            count=count+1
        dict.update({string[i]:count})
        j=j+1
    i=i+1
print(dict)
