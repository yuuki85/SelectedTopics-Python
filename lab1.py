#1. Declare Variables
a = 100
print(a)
a = 'Python programming'
print(a)
var_name = 'python_programming'
print(var_name)

print("\n")

#2. Numeric Variables
a = 5
print("Type of a", type(a))
b = 5.0
print("\nType of a", type(b))
c = 4 + 4j
print("\nType of a", type(c))

print("\n")

#3. Literals
# list literal
fruits = ["apple", "mango", "orange"]
print(fruits)
# tuple literal
numbers = (1, 2, 3)
print(numbers)
# dictionary literal
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'}
print(alphabets)
# set literal
vowels = {'a', 'e', 'i' , 'o', 'u'}
print(vowels)

print("\n")

#Try this
print('Twinkle, twinkle, little star,\n' + 
      '\tHow I wonder what you are!\n' + 
      '\t\tUp above the world so high\n\t\tLike a diamond in the sky.' +
      '\nTwinkle, twinkle, little star,' +
      '\n\tHow I wonder what you are')

print("\n")

#4.List data types
student_id = {112, 114, 116, 118, 115}
print(student_id)
print(type(student_id))
print("\n")

#5.Dictionary data types
capital_city = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}
print(capital_city)
capital_city = {'Malaysia': 'Kuala Lumpur', 'Italy': 'Rome', 'England': 'London'}
print(capital_city['Malaysia'])
print("\n")


#6. Implicit Type Conversion
integer_number = 123
float_number = 1.23
new_number = integer_number + float_number
# display new value and resulting data type
print("Value:",new_number)
print("Data Type:",type(new_number))
print("\n")

#7. Explicit Type Conversion
num_string = '12'
num_integer = 23
print("Data type of num_string before Type Casting:",type(num_string))
# explicit type conversion
num_string = int(num_string)
print("Data type of num_string after Type Casting:",type(num_string))
num_sum = num_integer + num_string
print("Sum:",num_sum)
print("Data type of num_sum:",type(num_sum))

print("\n")
#8. Using input()
num = input('Enter a number: ')
print('You Entered:', num)
print('Data type of num:', type(num))
print("\n")

#9. Import random
import random
# generate random numbers 1 - 6
d1 = random.randint(1, 6)
d2 = random.randrange(6) + 1
total = d1 + d2
print("You rolled a", d1, "and a", d2, "for a total of", total)
input("\n\nPress the enter key to exit.")
print("\n")

#10. Append method
numbers = [21, 34, 54, 12]
print("Before Append:", numbers)
# using append method
numbers.append(32)
print("After Append:", numbers)
print("\n")


#try this 1
base = int(input('Enter the base: '))
height = int(input('Enter the height: '))
area = base*height/2
print("The area of the triangle is:", area)
print("\n")

#try this 2
from datetime import date
start_date = date(1967, 2, 14)
end_date = date(2000, 1, 1)
days = (end_date - start_date).days
print("Ahmad is", days, "days old.")
print("\n")

#try this 3
food1 = str(input('Fav food 1: '))
food2 = str(input('Fav food 2: '))
new_food = food1 + food2
print("My new favorite food is:", new_food)
print("\n")

#try this 4
bill = float(input("Enter the restaurant bill total: "))

tip_15 = bill * 0.15
tip_20 = bill * 0.20

print("The 15% tip: RM",tip_15)
print("The 20% tip: RM",tip_20)
print("\n")
