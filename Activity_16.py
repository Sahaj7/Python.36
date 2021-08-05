def main():
    a=input_string()
    b=totuple(a)
    display(b)
def input_string():
    return input("Enter a String: ")
def totuple(a):
    b=list()
    for i in a.split(';'):
        c=i.split('=')
        b.append(tuple(c))
    return b
    
    

def display(b):
    print("the Tuple is: ",b)

main()
