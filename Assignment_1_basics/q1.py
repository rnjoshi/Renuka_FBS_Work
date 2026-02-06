# Write a program to calculate the percentage of student based on marks of any 5 subjects.

m1 = float(input('Enter marks of subject 1: '))
m2 = float(input('Enter marks of subject 2: '))
m3 = float(input('Enter marks of subject 3: '))
m4 = float(input('Enter marks of subject 4: '))
m5 = float(input('Enter marks of subject 5: '))
total = m1 + m2 + m3 + m4 + m5
percentage = (total / 500) * 100 
print(f'Total Marks: {total}.')
print(f'Percentage: {percentage} %')