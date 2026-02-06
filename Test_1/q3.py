# 3. Write a program to accept distance in kilometre and convert into metres and centimetres both

kilo_meter = float(input('Enetr Distance in Kilometer :- '))
meters = kilo_meter * 1000
centimeters = kilo_meter * 100000
print(f'Distance in Meter is {meters} m And Distance in Centimeter is {centimeters} cm.')