def add(a,b):
    c=a+b
    return c
def subtract(d,e):
    f=d-e
    return f
def multiply(x,y):
    z=x+y
    return z
def main():
    symbol=input("enter the symbol")
    if symbol=="+":
        print(add(5,6))
    elif symbol=="-":
        print(subtract(5,3))
    elif symbol=="*":
        print(multiply(2,4))
    else:
        pass
main()
