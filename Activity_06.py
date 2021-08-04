a=input("Enter 5 number: ")
b=a.split(',')
c=b[0:3]
d=b[::-1]
print("sliced list: ",c)
b[0]=0
b[-1]=0
c[0]=0
c[-1]=0
print("Replaced list1= ",b)
print("Replaced list2= ",c)

print("reverse list: ",d)
