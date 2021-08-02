a=input("Enter 5 number")
b=list(a)
c=b[0:3]
print("sliced list: ",c)
b[0]=0
b[-1]=0
c[0]=0
c[-1]=0
print("Replaced list1= ",b)
print("Replaced list2= ",c)
