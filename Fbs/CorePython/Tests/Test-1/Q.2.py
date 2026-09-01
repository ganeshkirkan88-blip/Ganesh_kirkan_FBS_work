#Write a program to calculate simple interest based on Principal, Rate and Time (SI = P*R*T/100)
P = int(input('Enter principle :'))
R = int(input('Enter rate :'))
T = int(input('Enter time :'))

Simple_interest = P*R*T/100

print(f'simple interest={Simple_interest} ')