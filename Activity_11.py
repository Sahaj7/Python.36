def main():
    a = input_number()
    b = input_number()
    summation = add(a, b)
    display(a, b, summation)
def input_number():
    return int(input("Enter a number"))
def add(a,b):
    return a+b
def display(a, b, summation):
    print("summation of ",a,"and ",b,"is ",summation)


main()
