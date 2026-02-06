# Write a Program to input two angles from user and find third angle of the triangle.

a = int(input('Enetr First Angle: '))
b = int(input('Enter Second Angle: '))
c = 180 - (a + b)
print(f'Third Angle of the Triangle is: {c}')