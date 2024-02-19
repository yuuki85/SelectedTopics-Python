import tkinter as tk
from tkinter import messagebox

# Define the different package types and services
PACKAGE_TYPES = ["Letter", "Box"]
SERVICES = ["Next Day Priority", "Next Day Standard", "2-day"]

# Create a tk window
root = tk.Tk()
root.title("Expressed Mutiara Delivery Charge Calculator")
root.geometry("500x400")

# Create a frame for the package type radio buttons
package_type_frame = tk.LabelFrame(root, text="Package Type")
package_type_frame.pack()

# Radio button for each package type
package_type_var = tk.IntVar()
# Enumerate = function that is able to add a counter to an iterable
for i, package_type in enumerate(PACKAGE_TYPES):
    package_type_radiobutton = tk.Radiobutton(package_type_frame, text=package_type, variable=package_type_var, value=i)
    package_type_radiobutton.pack()

# Create a frame for the service radio buttons
service_frame = tk.LabelFrame(root, text="Service")
service_frame.pack()

# Create a radio button for each service
service_var = tk.IntVar()
for i, service in enumerate(SERVICES):
    service_radiobutton = tk.Radiobutton(service_frame, text=service, variable=service_var, value=i)
    service_radiobutton.pack()

# Create a frame for the kilogram entry
kilogram_frame = tk.LabelFrame(root, text="Kilogram Weight")
kilogram_frame.pack()

# Create an entry for the kilogram weight
kilogram_entry = tk.Entry(kilogram_frame)
kilogram_entry.pack()

result_frame = tk.LabelFrame(root, text="Delivery Price")
result_frame.pack()

# Function to calculate the delivery charge
def calculate_delivery_charge():

    package_type = PACKAGE_TYPES[package_type_var.get()]
    service = SERVICES[service_var.get()]
    kilogram = float(kilogram_entry.get())

    # Calculate the delivery charge based on the package type, service, and kilogram weight
    if package_type == "Letter":
        if service == "Next Day Priority":
            if kilogram <= 2.0:
                delivery_charge = 12.00
                extra_charge = 0.00
            else:
                # Display error message for exceeding kilogram limit
                tk.messagebox.showerror("Error", "Letter package weight cannot exceed 2 kilograms.")
                return
        elif service == "Next Day Standard":
            if kilogram <= 4.0:
                delivery_charge = 10.50
                extra_charge = 0.00
            else:
                tk.messagebox.showerror("Error", "Letter package weight cannot exceed 4 kilograms.")
                return
        elif service == "2-day":
            tk.messagebox.showerror("Error", "2-day service is not available for letter packages.")
            return
    elif package_type == "Box":
        if service == "Next Day Priority":
            delivery_charge = 15.00
            if kilogram > 1.0:
                extra_charge = (kilogram - 1.0) * 2.00
            else:
                extra_charge = 0.00
        elif service == "Next Day Standard":
            delivery_charge = 11.00
            if kilogram > 1.0:
                extra_charge = (kilogram - 1.0) * 1.00
            else:
                extra_charge = 0.00
        elif service == "2-day":
            delivery_charge = 7.00
            if kilogram > 1.0:
                extra_charge = (kilogram - 1.0) * 0.50
            else:
                extra_charge = 0.00

    total_charge = delivery_charge + extra_charge

    # Display the breakdown of the calculation
    delivery_charge_label.config(text="Base Charge: RM{:.2f}\nExtra Charge(per kg): RM{:.2f}\nTotal Charge: RM{:.2f}".format(delivery_charge, extra_charge, total_charge))

# Create a button to calculate the delivery charge
calculate_delivery_charge_button = tk.Button(root, text="Calculate Delivery Charge", command=calculate_delivery_charge)
calculate_delivery_charge_button.pack()

# Create a label to display the breakdown of the calculation
delivery_charge_label = tk.Label(result_frame, text="")
delivery_charge_label.pack()

root.mainloop()
