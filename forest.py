# Python Program to find the area of triangle

a = 5
b = 6

# Uncomment below to take inputs from the user
# a = float(input('Enter first side: '))
# b = float(input('Enter second side: '))


# calculate the semi-perimeter
s = (a + b ) / 2

# calculate the area
area = (s*(s-a)*(s-b)*) ** 0.5
print('The area of the triangle is %0.2f' %area)
