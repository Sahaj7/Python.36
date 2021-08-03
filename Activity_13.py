def main():
    a=input_no()
    b=testprime(a)
    
def input_no():
    return int(input("enter an integer "))
def testprime(a):
    if a>1:
        for i in range(2,a):
            if(a%i)!=0:
                print(a, "is a prime number")
                break
            else:
                print(a, "is not a prime number")
                break
        else:
            print(a, "is not a prime number")
 
        
       
main()
