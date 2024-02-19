#1. If Statement
number = 5 
# outer if statement 
if (number >= 0): 
# inner if statement 
    if number == 0: 
        print('Number is 0') 
    # inner else statement 
    else: 
        print(number) 
        print('Number is positive') 
# outer else statement 
else: 
    print('Number is negative')
print("\n")


#2. While Statement
# program to calculate the sum of numbers
# until the user enters zero
total = 0
number = int(input('Enter a number: '))
# add nu#ers until number is zero
while number != 0:
    total+= number
    # take integer input again
    number = int(input('Enter a number:'))

print('total =', total)
print("\n")

#3. For...Else
fruits = ['banana', 'apple', 'mango'] 

for index in range(len(fruits)): 
    print('Current fruit :', fruits[index]) 
else: 
    print("Good bye!")
print("\n")


#4. def function 
def my_function(food): 
    for x in food: 
        print(x) 
fruits = ["apple", "banana", "cherry"] 
my_function(fruits)
print("\n")

#5. def function with * 
def my_function(*kids): 
    print("The youngest child is " + kids[2]) 
my_function("Ali", "Ahmad", "Atan")
print("\n")

#6. lambda 
def myfunc(n): 
    return lambda a : a * n
mynum = myfunc(2) 
print(mynum(11))
print("\n")

#7. len function 
message = input("Enter a message: ") 
print("\nThe length of your message is:", len(message)) 
print("\nThe most common letter in the English language, 'e',") 
if "e" in message: 
    print("is in your message") 
else: 
    print("is not in your message.") 
input("\n\nPress the enter key to exit.")

#8. While..If
i = 1 
while i < 6: 
    print(i) 
    i += 1 
else: 
    print("i is no longer less than 6")
print("\n")

#9. Import random
import random 
# generate random numbers 1 - 6 
num1 = random.randint(1, 6) 
num2 = random.randrange(6) + 1 
total = num1 + num2 
print("You generate a", num1, "and a", num2, "for a total of", total)
print("\n")

#10. Guess game
import random 
# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
# pick one word randomly from the sequence 
word = random.choice(WORDS) 
# create a variable to use later to see if the guess is correct 
correct = word 
# create a jumbled version of the word 
jumble ="" 
while word: 
    position = random.randrange(len(word))
    jumble += word[position] 
    word = word[:position] + word[(position + 1):] 

guess = input("\nYour guess: ")
while guess != correct and guess != "": 
    print("Sorry, that's not it.") 
    guess = input("Your guess: ") 
    
if guess == correct: 
    print("That's it! You guessed it!\n") 
    print("Thanks for playing.") 
input("\n\nPress the enter key to exit.")
print("\n")

#11. Tuple
# Empty tuple 
my_tuple = () 
print(my_tuple) 

# Tuple having integers
my_tuple = (1, 2, 3) 
print(my_tuple) 

# tuple with mixed datatypes 
my_tuple = (1, "Hello", 3.4) 
print(my_tuple)

# nested tuple 
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3)) 
print(my_tuple)
print("\n")

#12. Dictionary
student_id = {111: "Eric", 112: "Kyle", 113: "Butters"} 
print("Initial Dictionary: ", student_id) 
del student_id[111] 
print("Updated Dictionary ", student_id)
print("\n")

#Try this 1
integer1 = int(input("Enter a number: "))
integer2 = int(input("Enter a number: "))
total = integer1 + integer2

if 15 <= total <= 20:
    total = 20
    print(total)
else:
    print(total)
print("\n")

#Try this 2
alphabet = input("Please enter a single alphabet: ")

# Validate the input
if len(alphabet) == 1 and alphabet.isalpha():
    # Convert the input to lowercase 
    alphabet = alphabet.lower()

    # Determine whether the alphabet is a vowel or a consonant
    if alphabet in ['a', 'e', 'i', 'o', 'u']:
        print(f"The letter '{alphabet}' is a vowel.")
    else:
        print(f"The letter '{alphabet}' is a consonant.")
else:
    print("Invalid input. Please enter a single alphabet character.")
print("\n")

#Try this 3
start_number = int(input("Enter the starting number: "))
end_number = int(input("Enter the ending number: "))
count_by = int(input("Enter the amount by which to count: "))

# Perform the counting and display the results
if start_number <= end_number:
    print("Counting:")
    current_number = start_number
    while current_number <= end_number:
        print(current_number, end=" ")
        current_number += count_by
else:
    print("Error: The starting number should be less than or equal to the ending number.")
print("\n")

#Try this 4
import random

# Create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")

# Pick one word randomly from the sequence
word = random.choice(WORDS)
correct = word  # Store the correct word for later comparison

# Create a jumbled version of the word
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print("Welcome to the Try_This_4 Game!")
print("I've picked a word, and it's", len(correct), "letters long.")

# Allow the player five chances to ask if a letter is in the word
for _ in range(5):
    guess_letter = input("What letter is in the word: ").lower()
    if guess_letter in correct:
        print("Yes, '", guess_letter, "' is in the word.")
    else:
        print("No, '", guess_letter, "' is not in the word.")

# Now, let the player make the final guess
final_guess = input("\nNow, take a guess at the word: ").lower()

# Check if the final guess is correct
if final_guess == correct:
    print("Congratulations! You guessed the word!")
else:
    print("Sorry, that's not the word. The correct word was:", correct)

print("Thanks for playing!")
input("\n\nPress the enter key to exit.")
print("\n")


#Try this 5
num_rows = 9

for i in range(1, num_rows + 1):
    for j in range(i):
        print(i, end="")
    print()
print("\n")
