from math import sqrt
import cmath
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify_fraction(numer, denom):
    if denom == 0:
        return "Division by 0 - result undefined"
    common_divisor = gcd(numer, denom)
    (reduced_num, reduced_den) = (numer / common_divisor, denom / common_divisor)
    if common_divisor == 1:
        return (numer, denom)
    else:
        if (reduced_den > denom):
            if (reduced_den * reduced_num < 0):
                return(-reduced_num, -reduced_den)
            else:
                return (reduced_num, reduced_den)
        else:
            return (reduced_num, reduced_den)

def quadratic_factoring(a,b,c):
    if (b**2-4*a*c >= 0):
        x1 = (-b+sqrt(b**2-4*a*c))/(2*a)
        x2 = (-b-sqrt(b**2-4*a*c))/(2*a)
        mult1 = -x1 * a
        mult2 = -x2 * a
        (num1,den1) = simplify_fraction(a,mult1)
        (num2,den2) = simplify_fraction(a,mult2)
        if ((num1 > a) or (num2 > a)):
            print("No factorization")
        else:
            if (den1 > 0):
                sign1 = "+"
            else:
                sign1 = ""
            if (den2 > 0):
                sign2 = "+"
            else:
                sign2 = ""
            print("({}x{}{})({}x{}{})".format(int(num1),sign1,int(den1),int(num2),sign2,int(den2)))
    else:
        print("Solutions are imaginary")
    return
def quadratic_solve(a,b,c):
    d = (b**2) - (4*a*c)
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)
    print ("The Solutions Are:",sol1,"and",sol2)
    print ('Remember Solutions Are Always Opposite')

def quadratic_vertex_form(a,b,c):
    if a != 1: b /= a; xcoord= b/2; ycoord = c - a * (xcoord)
    else: xcoord = b/2; ycoord = c -(xcoord)
    if xcoord > 0: xsign = "+"
    else: xsign = ""
    if ycoord > 0: ysign = "+"
    else: ysign = "" 

    print(f"{a}(x {xsign} {xcoord}) {ysign} {ycoord}")
    

def distance_formula(x1,x2,y1,y2):
    distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    print ("The Distance Is:",distance)

question = int(input("1 for Factoring 2 for Solving 3 for Distance: "))


if (question == 1):
    a = float(input("Enter A Value: "))
    b = float(input("Enter B Value: "))
    c = float(input("Enter C Value: "))
    quadratic_factoring(a,b,c)
elif (question == 2):
    a = float(input("Enter A Value: "))
    b = float(input("Enter B Value: "))
    c = float(input("Enter C Value: "))
    quadratic_solve(a,b,c)
elif (question == 3):
    a = float(input("Enter X1"))
    b = float(input("Enter X2"))
    c = float(input("Enter Y1"))
    d = float(input("Enter Y2"))
    distance_formula(b,a,d,c)
elif question == 4:
    a = float(input('Enter the value of a'))
    b = float(input('Enter the value of b'))
    c = float(input('Enter the value of c')) 