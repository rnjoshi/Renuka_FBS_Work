# Program to Find the Roots of a Quadratic Equation

a = float(input('Enter Value of a: '))
b = float(input('Enter Value of b: '))
c = float(input('Enter Value of c: '))
d = b*b - 4*a*c
root1 = (-b + d**0.5) / (2*a)
root2 = (-b - d**0.5) / (2*a)
print(f'Root 1 is: {root1}')
print(f'Root 2 is: {root2}')