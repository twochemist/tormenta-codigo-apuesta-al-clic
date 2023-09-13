import tkinter as tk
import random

# Define the list of lucky numbers
lucky_numbers = [7, 1]

# Function to generate a random number and check if it's lucky
def spin():
    result = random.randint(1, 10)
    if result in lucky_numbers:
        result_label.config(text=f"Congratulations! You win {result}!")
    else:
        result_label.config(text=f"Sorry, you got {result}. Try again!")

# Create the main window
window = tk.Tk()
window.title("Russian Roulette with Lucky Numbers")

# Create a button to spin the "roulette"
spin_button = tk.Button(window, text="Spin the Roulette", command=spin)
spin_button.pack(pady=20)

# Create a label to display the result
result_label = tk.Label(window, text="", font=("Helvetica", 16))
result_label.pack()

# Start the GUI event loop
window.mainloop()