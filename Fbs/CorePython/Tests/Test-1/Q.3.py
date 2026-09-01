#Write a program to accept distance in km and convert into meters and centimeters both

KM = int(input('Enter distance in kilometer:'))

meters = KM * 1000
centimeters = KM * 100000

print(f'Distance in meters :{ meters}')
print(f'Distance in centimeters : {centimeters}')