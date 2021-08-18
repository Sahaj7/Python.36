def main():
    a={}
    b=number()
    for i in range(b):
        key=input("Enter a key: ")
        value=input("Enter the value: ")
        a[key]=value
    print("Before Sort: ",a)
    from collections import OrderedDict
    dict1 = OrderedDict(sorted(a.items()))
    print("After sort: ",dict(dict1))
def number():
    n=int(input("Enter the number of items: "))
    return n

main()
    
