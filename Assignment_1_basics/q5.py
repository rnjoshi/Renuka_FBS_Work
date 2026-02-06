# Write a program to enter P, T, R and calculate Compound Interest.

p = float(input('Enter Principle(P): '))
t = float(input('Enter Time(T): '))
r = float(input('Enter Rate Of Interest(R)'))
ci = p * (1 + r/100) ** t - p
print(f'Compound Interest is: {ci}')