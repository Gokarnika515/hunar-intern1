import tkinter as tk
from tkinter import messagebox

def find_runner_up():
    try:
        # Get the list of scores from the entry widget
        scores = entry_scores.get().split()
        # Convert the scores to integers
        scores = [int(score) for score in scores]
        
        # Remove duplicates and sort the scores in descending order
        unique_scores = list(set(scores))
        unique_scores.sort(reverse=True)
        
        if len(unique_scores) < 2:
            raise ValueError("Not enough unique scores to determine the runner-up.")
        
        # The runner-up score is the second highest unique score
        runner_up_score = unique_scores[1]
        
        # Display the runner-up score
        messagebox.showinfo("Runner-Up Score", f"The runner-up score is: {runner_up_score}")
    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))
    except Exception as e:
        messagebox.showerror("Error", "An error occurred while processing the scores.")

# Create the main window
root = tk.Tk()
root.title("Runner-Up Score Finder")

# Create and place the label and entry widget for scores input
tk.Label(root, text="Enter scores separated by spaces:").grid(row=0, column=0, padx=10, pady=10)
entry_scores = tk.Entry(root, width=50)
entry_scores.grid(row=0, column=1, padx=10, pady=10)

# Create and place the button to find the runner-up score
button_find = tk.Button(root, text="Find Runner-Up", command=find_runner_up)
button_find.grid(row=1, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
