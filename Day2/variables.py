# Day 2: 30 Days of python programming

# Declaring variables
first_name = 'Hidayah'
last_name = 'Dayyib'
full_name = first_name + ' ' + last_name
country = 'Nigeria'
city = 'Kano'
age = 25
year = 2025
is_married = True
is_true = False
is_light_on = True

# Declaring multiple variables in one line
a, b, c = 5, 10, 15

# Printing variables
print('First Name:', first_name)
print('Last Name:', last_name)
print('Full Name:', full_name)
print('Country:', country)
print('City:', city)
print('Age:', age)
print('Year:', year)
print('Married:', is_married)
print('Is True:', is_true)
print('Is Light On:', is_light_on)
print('Multiple variables:', a, b, c)

# Checking data types of all variables
print('\nData Type Check')
print('Data type of first_name:', type(first_name))
print('Data type of age:', type(age))
print('Data type of is_married:', type(is_married))

# Length of first name
print('Length of first name:', len(first_name))

# Comparing lengths of first and last name
print('Is first name longer than last name?', len(first_name) > len(last_name))

# Arithmetic operations
num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

# Printing arithmetic results
print('\nArithmetic Operations')
print('Total:', total)
print('Difference:', diff)
print('Product:', product)
print('Division:', division)
print('Remainder:', remainder)
print('Exponentiation:', exp)
print('Floor Division:', floor_division)

# Circle calculations
import math
radius = 30
area_of_circle = math.pi * radius ** 2
circum_of_circle = 2 * math.pi * radius

print('\nCircle Calculations')
print('Area of Circle:', area_of_circle)
print('Circumference of Circle:', circum_of_circle)

# Asking for user input
user_radius = float(input('Enter a radius: '))
user_area = math.pi * user_radius ** 2
print('User-provided radius area:', user_area)

first_name_input = input('Enter your first name: ')
last_name_input = input('Enter your last name: ')
country_input = input('Enter your country: ')
age_input = input('Enter your age: ')
print(f'Hello, {first_name_input} {last_name_input}! You are from {country_input} and are {age_input} years old.')

# Check Python keywords
print('\nPython Keywords:')
help('keywords')
