# Write a program to enter P, T, R and calculate simple Interest.

p = float(input('Enter Principle(P): '))
t = float(input('Enter Time(T): '))
r = float(input('Enter Rate Of Interest(R)'))
si = p * r * t / 100
print(f'Simple Interest is: {si}')