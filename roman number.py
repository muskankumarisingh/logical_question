number=int(input("enter integer"))
a=["","M","MM","MMM"]
b=["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
c=["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
d=["","I","II","III","IV","V","VI","VII","VIII","IX"]
e=a[number//1000]
f=b[(number%1000)//100]
tens=c[(number%100)//10]
g=d[number%10]
ROMAN=(e+f+tens+g)
print(ROMAN)
