from pdf2docx import Converter
from docx2pdf import convert
import os
from pdf2image import convert_from_path
from pikepdf import Pdf,Page,Rectangle
import tkinter as tk  # Import the tkinter module for GUI
from tkinter import*
from fpdf import FPDF  # Importing FPDF library for PDF generation
import os  # Importing os module for interacting with the operating system
import time  # Import the time module for working with time
from time import strftime

# from pdf2docx import Converter
def pdf2Word():
    # inputs/tat.pdf
    o_pdf = input("Enter the file name(PDF): ")
    #  outputs/TAT_OUT.docx
    n_docx = input("Enter the new file name you want to assign(add .docx): ")

    obj = Converter(o_pdf)
    obj.convert(n_docx)
    obj.close()
    print("Pdf converted to word successfully \n\n")
# ------------------------------------------------------------------------------------

# from docx2pdf import convert

def word2pdf():
    # inputs/task2.docx
    o_docx = input("Enter the file name(add .docx): ")
    # outputs/TASK_2.pdf
    n_pdf = input("Enter the new file name you want to assign(add .pdf): ")

    convert(o_docx,n_pdf)
    print("Word converted to pdf successfully \n\n")

# ------------------------------------------------------------------------------------

# from pdf2image import convert_from_path
def pdf2Img():
    # inputs/tat.pdf
    pdfname = input("Enter the pdf name(add .pdf): ") 
    o_pdf = convert_from_path(pdfname,poppler_path=r"D:\CLG\SEM-3\Projects\poppler-23.11.0\Library\bin")

    # counting pages and cerating images

    for i in range(len(o_pdf)):
        o_pdf[i].save("n_"+str(i+1)+".jpg","JPEG")

    print("Pdf Converted to images\n\n")

# -----------------------------------------------------------------------------------

# from pikepdf import Pdf,Page,Rectangle
def watermark():
    # inputs/tat.pdf
    f1 = input("Enter the background file name(add .pdf)")
    # inputs/int.pdf
    f2 = input("Enter the watermark file(.pdf)")
    # Enter the output file name
    outf = input("Enter the output file name(add .pdf)")
    o_pdf1 = Pdf.open(f1)
    o_pdf2 = Pdf.open(f2)

    destination_page = Page(o_pdf1.pages[0])
    source_page = Page(o_pdf2.pages[0])

    destination_page.add_overlay(source_page,Rectangle(0,0,150,150))
    o_pdf1.save(outf)

    print("Successfully  added Watermark \n\n")

# -----------------------------------------------------------------------------------

def basicCalc():
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


# ---------------------------------------------------------------------------------------

def digitalClock():
    # creating tkinter window
    root = Tk()
    root.title('Clock')

    # This function is used to display time on the label

    def time():
        string = strftime('%H:%M:%S %p')
        lbl.config(text=string)
        lbl.after(1000, time)


    # Styling the label widget so that clock will look more attractive
    lbl = Label(root, font=('calibri', 40, 'bold'),
                background='cyan',
                foreground='black')

    # Placing clock at the centre of the tkinter window
    lbl.pack(anchor='center')
    time()

    mainloop()

# -----------------------------------------------------------------------------------------
# from fpdf import FPDF  # Importing FPDF library for PDF generation
# import os  # Importing os module for interacting with the operating system

def img2Pdf():
    pdf = FPDF()  # Creating an instance of the FPDF class to work with PDFs
    pdf.set_auto_page_break(0)  # Disabling auto page break to manually control page breaks
# Imagesss
    loc = input("Enter the Folder Location: ")

    # Creating a list to store the names of all images in a folder
    # Note: You can also ask the user to input the path where images are located
    img_list = [x for x in os.listdir(loc)]

    # Iterating through each image in the list
    for img in img_list:
        pdf.add_page()  # Adding a new page to the PDF for each image
        image = "Imagesss\\" + img  # Constructing the path of the image file
        pdf.image(image)  # Adding the image to the PDF page

    pdf.output("imagesCon.pdf")  # Saving the PDF with all images added
    print("Successfully converted")  # Printing a success message after PDF creation


# ------------------------------------------------------------------------------------------

def StopWatch():
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


# ------------------------- MAIN --------------------------------

print("\t\t Hello Pal!\n")
print("\t     Get Ready To Work\n")

while True:
    print("""\t 1. Convert Pdf -> Word \n
         2. Convert word -> Pdf \n
         3. Convert Pdf -> Image/s \n
         4. Convert Images -> pdf \n
         5. Add Watermark \n 
         6. Basic Calculator \n
         7. Digital Clock \n 
         8. Stop Watch \n\n""")
    
    print("\tPRESS '-1' TO EXIT")
    choice = int(input("Enter your choice: "))

    if(choice == 1): pdf2Word()
    elif(choice==2): word2pdf()
    elif(choice==3): pdf2Img()
    elif(choice==4): img2Pdf()
    elif(choice==5): watermark() 
    elif(choice==6): basicCalc()
    elif(choice==7): digitalClock()
    elif(choice==8): StopWatch()
    elif(choice==-1): break
    else: continue
    
print("See You soon! \n")
print("\t Buddy")

