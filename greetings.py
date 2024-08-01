import tkinter as tk
from tkinter import messagebox

# Function to generate the greeting message
def generate_greeting():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    if first_name and last_name:
        greeting_message = f"Hello, {first_name} {last_name}! Welcome!"
        messagebox.showinfo("Greeting Message", greeting_message)
    else:
        messagebox.showwarning("Input Error", "Please enter both your first and last names.")

# Create the main window
root = tk.Tk()
root.title("Greeting Message Generator")

# Create and place the labels and entry widgets for first and last names
tk.Label(root, text="First Name:").grid(row=0, column=0, padx=20, pady=20)
entry_first_name = tk.Entry(root)
entry_first_name.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Last Name:").grid(row=1, column=0, padx=10, pady=10)
entry_last_name = tk.Entry(root)
entry_last_name.grid(row=1, column=1, padx=20, pady=20)

# Create and place the button to generate the greeting message
button_generate = tk.Button(root, text="Generate Greeting", command=generate_greeting)
button_generate.grid(row=2, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
