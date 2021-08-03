def characteristic_dimension(l,b,h):
    return float((l**2)+(b**2)+(h**2))
def denominator(k):
    return float(k**(1/2))
def numerator(b,l):
    return float((b**2)*(l**2))
def volume(num,den):
    return float(num/den)
def radius(v):
    return float(((3*v)/(4*3.14))**(1/3))
    

def main():
    l=int(input("Enter the value of length "))
    b=int(input("Enter the value of breadth "))
    h=int(input("Enter the value of height "))
    k=characteristic_dimension(l,b,h)
    den=denominator(k)
    num=numerator(b,l)
    v=volume(num,den)
    x=round(v,3)
    print("Volume of Tromboloid=",x)
    r=radius(v)
    print("Radius of the sphere having the same volume = ",format(r,".3f"))

main()
