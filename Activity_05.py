a=input("Enter 5 numbers")
b=a.split()
l=list(b)
print(l)
sum=0
for i in l:
    sum=sum+int(i)
print("The sum of all the number = ",sum)
