import random
from tkinter import *

# List of item counts
location_options = ["Cali", "Florida"]

# Dictionary of suggestions
suggestions = {
    "Theft": ["Get a door camera", "Get a home security system", "Lock your door and windows", "Purchase blinds and/or curtains"],
    "Fire": ["Buy an new smoke alarm", "Buy a fire extinguisher", "Purchase Kitchen and Laundry Inspection"],
    "Flood": ["Build flood wall around house", "Seal doors and windows", "Install sump pump", "Install backwater valves"],
    "Wild Fire": ["Install clay or metal roof"]
}

def generate_checklist():
    location = num_items_var.get()

    # Initialize suggestion list with theft and fire suggestions
    suggestion_list = suggestions["Theft"] + suggestions["Fire"]

    if location == "Cali":
        # Add wild fire suggestions for Cali
        suggestion_list += suggestions["Wild Fire"]
    elif location == "Florida":
        # Add flood suggestions for Florida
        suggestion_list += suggestions["Flood"]

    # Shuffle the suggestion list
    random.shuffle(suggestion_list)

    # Display suggestions with checkboxes
    for index, suggestion in enumerate(suggestion_list[:5]):
        Checkbutton(root, text=suggestion, variable=checkbox_vars[index]).grid(row=index + 3, column=0, columnspan=2, padx=10, pady=5)

root = Tk()
root.title("Randomly Generated Checklist")

num_items_label = Label(root, text="Choose your location:")
num_items_label.grid(row=0, column=0, padx=10, pady=5)

num_items_var = StringVar()
num_items_dropdown = OptionMenu(root, num_items_var, *location_options)
num_items_dropdown.grid(row=0, column=1, padx=10, pady=5)
num_items_var.set("Cali")  # Set default value

generate_button = Button(root, text="Generate", command=generate_checklist)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# Variables to track the state of checkboxes
checkbox_vars = [IntVar() for _ in range(5)]

root.mainloop()
