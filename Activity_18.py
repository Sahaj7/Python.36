def main():
    a=input_string()
    b=todictionary(a)
    c=convertdict(b)
    display(c)
def input_string():
    return input("Enter a String: ")
def todictionary(a):
    b=list()
    for i in a.split(';'):
        c=i.split('=')
        b.append(tuple(c))
    return b
def convertdict(b):
    c=dict(b)
    return c

    
    
    

def display(c):
    print("the dictionary is: ",c)

main()
