list=[1,4,9,10,12,13,7,6,2]
i=0
even_sum=0
odd_sum=0
while i<len(list):
    if i%2==0:
        even_sum=even_sum+list[i]
        avg_even=even_sum/5
    else:
        odd_sum=odd_sum+list[i]
        avg_odd=odd_sum/4
    i=i+1
print(avg_even)
print(avg_odd)