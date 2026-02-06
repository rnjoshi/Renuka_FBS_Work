#Convert distant given in feet and inches into meter and centimeter.

feet = float(input('Enter The Distance in Feet = '))
inches = float(input('Enter The Distance in Inches = '))
meter = (feet * 0.3048) + (inches * 0.0254)
cm = meter * 100
print(f'Distance in Meter = {meter}.m')
print(f'distance in CentiMeter = {cm}.cm')
 