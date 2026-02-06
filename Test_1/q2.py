# 2. Write a program to calculate simple interest based on principle, rate and time (SI = P*R*T/100)

p = float(input('Enter Principle(P) :- '))
t = float(input('Enter Time(T) :- '))
r = float(input('Enter Rate Of Interest(R) :- '))
si = p * r * t / 100
print(f'Simple Interest is :- {si}')