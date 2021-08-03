
def input_string():
    return input("Enter a sentence")
def display(b):
    print("using sorted(): ",sorted(b))
    print("original list: ",b)
    print("using sort")
    b.sort()
    print(b)
    
def main():
    a=input_string()
    b=a.split()
    display(b)



main()
