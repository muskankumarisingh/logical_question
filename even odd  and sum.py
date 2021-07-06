list=[2,5,8,10,12,6,9,15,22,42]
i=0
even_sum=0
odd_sum=0
while i<len(list):
    if list[i]%2==0:
        even_sum=even_sum+list[i]
    else:
        odd_sum=odd_sum+list[i]
    i=i+1
print(even_sum)
print(odd_sum)