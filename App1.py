import tkinter as tk
from tkinter import ttk

def calculate_weight():
    # Step 1: Get the user's weight on Earth
    earth_weight = float(entry_earth_weight.get())

    # Step 2: Define gravity multipliers for each planet
    mercury_multiplier = 0.4
    venus_multiplier = 0.9
    jupiter_multiplier = 2.5
    saturn_multiplier = 1.1

    # Step 3: Calculate weight on each planet
    mercury_weight = earth_weight * mercury_multiplier
    venus_weight = earth_weight * venus_multiplier
    jupiter_weight = earth_weight * jupiter_multiplier
    saturn_weight = earth_weight * saturn_multiplier

    # Step 4: Display the results
    result_text.set(
        f"Weight on each planet:\n"
        f"Mercury: {mercury_weight:.2f} kg\n"
        f"Venus: {venus_weight:.2f} kg\n"
        f"Jupiter: {jupiter_weight:.2f} kg\n"
        f"Saturn: {saturn_weight:.2f} kg"
    )

# Create the main window
root = tk.Tk()
root.title("Weight Converter")

# Create and place widgets
label_earth_weight = ttk.Label(root, text="Enter your weight on Earth (in kilograms):")
label_earth_weight.grid(row=0, column=0, padx=10, pady=10, sticky="W")

entry_earth_weight = ttk.Entry(root)
entry_earth_weight.grid(row=0, column=1, padx=10, pady=10, sticky="W")

calculate_button = ttk.Button(root, text="Convert", command=calculate_weight)
calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

result_text = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_text)
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()
