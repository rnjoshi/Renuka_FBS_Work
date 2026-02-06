# Write a program to accept an integer amount from user and tell minimum 
# number of notes needed for representing that amount.

amount = int(input('Enter amount: '))

count = amount // 2000
amount = amount % 2000
print(f'2000: {count}')

count = amount // 500
amount = amount % 500
print(f'500: {count}')

count = amount // 100
amount = amount % 100
print(f'100: {count}')

count = amount // 50
amount = amount % 50
print(f'50: {count}')

count = amount // 20
amount = amount % 20
print(f'20: {count}')

count = amount // 10
amount = amount % 10
print(f'10: {count}')

count = amount // 5
amount = amount % 5
print(f'5: {count}')

count = amount // 2
amount = amount % 2
print(f'2: {count}')

count = amount // 1
print(f'1: {count}')
