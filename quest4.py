import random

def generate_random_numbers():
    # Generates three random numbers between 0 and 9.
    numbers = []
    for i in range(3):
        numbers.append(random.randint(0, 9))
    return numbers

def get_hint(guess, secret_numbers):
    # Returns a hint for the given guess and secret numbers.
    hint = ""

    for i in range(3):
        if guess[i] == secret_numbers[i]:
            hint += "Fermi "
        elif guess[i] in secret_numbers:
            hint += "Pico "
        else:
            hint += "Nano "

    return hint.strip()

def is_valid_input(guess_str):
    # Checks if the user input contains three numbers separated by spaces.
    try:
        numbers = [int(num) for num in guess_str.split()]
        return len(numbers) == 3
    except ValueError:
        return False

def play_game():
    secret_numbers = generate_random_numbers()

    num_guesses = 0

    while True:
        guess_str = input("Enter your guess (three numbers separated by space): ")

        # Check if the user wants to quit
        if guess_str.lower() == "quit":
            print(f"The correct answer was: {secret_numbers}")
            print("Thank you for playing!")
            print("Number of guesses:", num_guesses)
            input("\n\nPress the enter key to exit.")
            break
        
        # Check if the user input is valid
        if not is_valid_input(guess_str):
            print("Invalid input. Please enter three numbers separated by spaces.")
            continue
        
        # Convert the user input (guess) into a list of integers
        guess = [int(num) for num in guess_str.split()]

        # Check if the guess is correct
        hint = get_hint(guess, secret_numbers)
        num_guesses += 1

        if hint == "Fermi Fermi Fermi":
            print("You guessed correctly!")
            print("Correct answer:", secret_numbers)
            print("Number of guesses:", num_guesses)
            input("\n\nPress the enter key to exit.")
            break

        print("Hint:", hint)

play_game()
