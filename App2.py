import tkinter as tk
from tkinter import ttk

def apply_variation():
    # Get user input
    original_sentence = entry_sentence.get()

    # Get user choice for variation
    variation_choice = variation_combobox.get()

    # Apply the selected variation
    words = original_sentence.split()

    if variation_choice == 'Sha':
        result = [f"sha{word}" for word in words]
    elif variation_choice == 'Na':
        result = [f"{word}na" for word in words]
    elif variation_choice == 'Sha Na Na':
        result = [f"sha{word}na na" for word in words]
    elif variation_choice == 'Ava':
        result = [f"{word[1:]}{word[0]}ava" for word in words]
    else:
        result = []

    # Display the result
    output_sentence = ' '.join(result)
    result_text.set(output_sentence)

# Create the main window
root = tk.Tk()
root.title("Eggy-Peggy Word Variations")

# Create and place widgets
label_sentence = ttk.Label(root, text="Enter a sentence:")
label_sentence.grid(row=0, column=0, padx=10, pady=10, sticky="W")

entry_sentence = ttk.Entry(root)
entry_sentence.grid(row=0, column=1, padx=10, pady=10, sticky="W")

label_variation = ttk.Label(root, text="Select a variation:")
label_variation.grid(row=1, column=0, padx=10, pady=10, sticky="W")

variation_choices = ['Sha', 'Na', 'Sha Na Na', 'Ava']
variation_combobox = ttk.Combobox(root, values=variation_choices)
variation_combobox.grid(row=1, column=1, padx=10, pady=10, sticky="W")

apply_button = ttk.Button(root, text="Apply Variation", command=apply_variation)
apply_button.grid(row=2, column=0, columnspan=2, pady=10)

result_text = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_text)
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()
