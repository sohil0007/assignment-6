print("Enter a Value of a,b and c")

a,b,c = int(input()),int(input()),int(input())

d = b**2 - 4*a*c

if d>0:
    print("real & distinct roots")

elif d==0:
    print("real & equal roots")

else :
    print("imaginary roots")
    
