def main():
    print("Enter 1 to add")
    print("Enter 2 to sub")
    print("Enter 3 to multiply")
    print("Enter 4 to divide")
    ch=int(input())
    a=int(input("Enter the value of A ? "))
    b=int(input("Enter the value of B ? "))
    if ch==1:
        result=add(a,b)
    elif ch==2:
        result=sub(a,b)
    elif ch==3:
        result=multi(a,b)
    else:
        result=div(a,b)

    print("Result of the operation is ",result)


def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    return a/b

print("first priority")
print(__name__)
if __name__=="__main__":
    
    main()
print("third")
    
