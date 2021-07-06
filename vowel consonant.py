vowel=("a","e","i","o","u")
count = 0
count1 = 0 
num= input("enter sentence")
i=0
while i<len(num):  
    if num[i] in vowel:  
        count = count + 1  
    elif (num[i] >= 'a' and num[i] <= 'z'):  
        count1 = count1 + 1
    i+=1  
print("vowel:",count) 
print("consonent:",count1) 
