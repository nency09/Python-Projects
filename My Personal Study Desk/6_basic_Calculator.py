import tkinter as tk  # Import the tkinter module for GUI

def on_button_click(event):
    # Get the button text
    text = event.widget.cget("text")
    # Perform calculation based on the button clicked
    if text == "=":  # If the button clicked is "=", perform calculation
        try:
            result = eval(entry.get())  # Evaluate the expression in the entry widget
            # formatted_result = "{:.2f}".format(result)
            entry.delete(0, tk.END)  # Delete the current content in the entry widget
            entry.insert(tk.END, result)  # Insert the result into the entry widget / result(formatted_result)
        except Exception as e:  # Handle exceptions such as division by zero
            entry.delete(0, tk.END)  # Delete the current content in the entry widget
            entry.insert(tk.END, "Error")  # Display error message
    elif text == "C":  # If the button clicked is "C", clear the entry widget
        entry.delete(0, tk.END)  # Delete the current content in the entry widget
    else:  # If a digit or operator button is clicked, add it to the entry widget
        entry.insert(tk.END, text)  # Insert the button text into the entry widget

# Create the main window
root = tk.Tk()  # Create an instance of the Tk class
root.title("Basic Calculator")  # Set the title of the window

# Create entry widget for displaying input and output
entry = tk.Entry(root, width=25, font=('Arial', 14))  # Create an entry widget
entry.grid(row=0, column=0, columnspan=4)  # Place the entry widget in the first row

# Define button labels
buttons = [
    "7", "8", "9", "/",  # Digit buttons and division operator
    "4", "5", "6", "*",  # Digit buttons and multiplication operator
    "1", "2", "3", "-",  # Digit buttons and subtraction operator
    "C", "0", "=", "+"   # Clear button, digit zero, equal sign, and addition operator
]

# Create and place buttons in a grid
row = 1  # Start from the second row
col = 0  # Start from the first column
for button_label in buttons:
    button = tk.Button(root, text=button_label, width=5, height=2, font=('Arial', 12))  # Create a button
    button.grid(row=row, column=col)  # Place the button in the grid
    col += 1  # Move to the next column
    if col > 3:  # If the column exceeds 4, reset it to 0 and move to the next row
        col = 0
        row += 1

# Bind button clicks to the function
root.bind("<Button-1>", on_button_click)  # Bind left mouse button click event to on_button_click function

# Run the main event loop
root.mainloop()  # Start the event loop to display the GUI and handle user interactions
