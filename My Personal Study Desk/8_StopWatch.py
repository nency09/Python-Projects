import tkinter as tk  # Import the tkinter module for GUI
import time  # Import the time module for working with time

class Timer:
    def __init__(self, root):
        self.root = root  # Store the root window reference
        self.root.title("Timer")  # Set the title of the root window

        self.running = False  # Flag to track if the timer is running or not
        self.start_time = None  # Variable to store the start time of the timer
        self.elapsed_time = 0  # Variable to store the elapsed time

        # Create a label to display the time
        self.label = tk.Label(root, text="00:00:00", font=("Arial", 24))
        self.label.pack(pady=10)  # Place the label in the window with some padding

        # Create a button to start the timer
        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=10)  # Place the button on the left side with padding

        # Create a button to stop the timer
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_timer)
        self.stop_button.pack(side=tk.LEFT, padx=10)  # Place the button on the left side with padding
        self.stop_button.config(state=tk.DISABLED)  # Initially disable the stop button

        # Create a button to reset the timer
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer)
        self.reset_button.pack(side=tk.RIGHT, padx=10)  # Place the button on the right side with padding

        # Initialize the timer display
        self.update_time()

    def start_timer(self):
        if not self.running:  # If the timer is not running
            self.running = True  # Set the running flag to True
            self.start_time = time.time() - self.elapsed_time  # Record the start time
            self.start_button.config(state=tk.DISABLED)  # Disable the start button
            self.stop_button.config(state=tk.NORMAL)  # Enable the stop button
            self.update_time()  # Update the time display

    def stop_timer(self):
        if self.running:  # If the timer is running
            self.running = False  # Set the running flag to False
            self.start_button.config(state=tk.NORMAL)  # Enable the start button
            self.stop_button.config(state=tk.DISABLED)  # Disable the stop button

    def reset_timer(self):
        self.running = False  # Set the running flag to False
        self.start_button.config(state=tk.NORMAL)  # Enable the start button
        self.stop_button.config(state=tk.DISABLED)  # Disable the stop button
        self.start_time = None  # Reset the start time
        self.elapsed_time = 0  # Reset the elapsed time
        self.update_time()  # Update the time display

    def update_time(self):
        if self.running:  # If the timer is running
            self.elapsed_time = time.time() - self.start_time  # Calculate the elapsed time
        hours, remainder = divmod(self.elapsed_time, 3600)  # Calculate hours
        minutes, seconds = divmod(remainder, 60)  # Calculate minutes and seconds
        # Format the time string as HH:MM:SS
        time_string = "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))
        self.label.config(text=time_string)  # Update the label text with the time string
        self.root.after(1000, self.update_time)  # Schedule the update_time method to be called again after 1 second

# Create the root window
root = tk.Tk()
# Create an instance of the Timer class with the root window as an argument
timer = Timer(root)
# Start the Tkinter event loop
root.mainloop()
