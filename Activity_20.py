def main():
    a={}
    b=number()
    for i in range(b):
        key=input("Enter a key: ")
        value=input("Enter the value: ")
        a[key]=value
    print("Before sorting: ",a)
    sortedvalues = sorted(a.values())
    dict1={}
    for i in sortedvalues:
        for k in a.keys():
            if a[k]==i:
                dict1[k]=a[k]
                break
    print("After sorting: ",dict1)
def number():
    n=int(input("Enter the number of elements in dictionary: "))
    return n
main()
