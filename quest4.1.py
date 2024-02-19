import random
import tkinter as tk
from tkinter import messagebox

def generate_random_numbers():
    # Generates three random numbers between 0 and 9.
    return [random.randint(0, 9) for _ in range(3)]

def get_hint(guess, secret_numbers):
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
    try:
        numbers = [int(num) for num in guess_str.split()]
        return len(numbers) == 3
    except ValueError:
        return False

def play_game():
    secret_numbers = generate_random_numbers()
    num_guesses = 0

    root = tk.Tk()
    root.title("Number Guessing Game")

    label = tk.Label(root, text="Enter your guess (three numbers separated by space):")
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    def check_guess():
        nonlocal num_guesses
        guess_str = entry.get().lower()

        if not is_valid_input(guess_str):
            messagebox.showinfo("Invalid Input", "Please enter three numbers separated by spaces.")
            return

        guess = [int(num) for num in guess_str.split()]
        hint = get_hint(guess, secret_numbers)
        num_guesses += 1

        if hint == "Fermi Fermi Fermi":
             messagebox.showinfo("Congratulations!", f"You guessed correctly!\nCorrect answer: {secret_numbers}\nNumber of guesses: {num_guesses}")
             root.destroy()
        else:
            result_label.config(text=f"Hint: {hint}")

    def quit_game():
        messagebox.showinfo("Game Over", f"The correct answer was: {secret_numbers}\nNumber of guesses: {num_guesses}")
        root.destroy()

    button = tk.Button(root, text="Submit Guess", command=check_guess)
    button.pack()

    quit_button = tk.Button(root, text="Quit", command=quit_game)
    quit_button.pack()

    result_label = tk.Label(root, text="")
    result_label.pack()

    root.mainloop()

play_game()
