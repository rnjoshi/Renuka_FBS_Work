#Find the sum of three-digit number.

num = int(input('Enter the Number= '))
r1 = num % 10
num = num // 10
r2 = num % 10
num = num // 10
r3 = num % 10
print(f'r1 = {r1} r2 = {r2} r3 = {r3} num = {num}')
sum = r1 + r2 + r3
print(f'Sum of Three Digit Number = {sum}.')