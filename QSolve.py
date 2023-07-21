# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath

a = float(input("Enter Value A: "))
b = float(input("Enter Value B: "))
c = float(input("Enter Value C: "))
def quadratic_solve(a,b,c):
# calculate the discriminant
    d = (b**2) - (4*a*c)

# find two solutions
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)
    print ("The Solutions Are:",sol1,"and",sol2)

quadratic_solve(a,b,c)
print ('Remember Solutions Are Always Opposite')