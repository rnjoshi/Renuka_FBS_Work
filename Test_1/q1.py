# 1. Write a Program to Find the area and perimeter of the following
# (Accept the length,breadth and radious from user)

l = int(input('Enetr Length :- '))
b = int(input('Enter Breadth :- '))
r = int(input('Enetr Radious :- '))

rect_area = l * b
rect_pera = 2 * (l + b)

circle_area = 3.14 * r * r
circle_pera = 2 * 3.14 * r

print(f'Area of Rectangle is :- {rect_area} And  Perimeter Of Rectangle is :- {rect_pera}')
print(f'Area of Circle is :- {circle_area} And  Perimeter Of Circle is :- {circle_pera}')

