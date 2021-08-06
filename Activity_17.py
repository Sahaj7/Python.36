def main():
    a=input_tuple()
    b=tostring(a)
    display(b)
def input_tuple():
    return input("Enter the tuple: ")
    
def tostring(a):
    b=str()
    for i in a.split('), ('):
        c=i.split(',')
        b=b+c[0]+"="+c[1]+"; "
        b=b.rstrip(';')
    b=b.replace("'",'')
    b=b.replace('[(','')
    b=b.replace(')]','')
        
    return b


def display(b):
    print("The string is: ",b)

main()
