def main():
    a=input_no()
    b=input_no()
    c=input_no()
    d=greatest(a,b,c)
    display(a,b,c,d)
def input_no():
    return int(input("Enter a number"))
def greatest(a,b,c):
    return max(a,b,c)
def display(a,b,c,d):
    print(d," is the greatest number among ",a,b,c)


main() 
    
