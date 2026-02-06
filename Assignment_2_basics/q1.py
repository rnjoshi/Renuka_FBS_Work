#Convert the time entered in hh,min and sec into seconds.

hh =  int(input('Enter the Hours= '))
min = int(input('Enter the Minutes= '))
sec = int(input('Enter the Second= '))
total_seconds = hh * 3600 + min * 60 + sec
print(f'Total Seconds  = {total_seconds}.')