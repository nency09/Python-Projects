from tkinter import *
from pdf2docx import Converter
from docx2pdf import convert
import os
from pdf2image import convert_from_path
from pikepdf import Pdf,Page,Rectangle
from time import strftime
from fpdf import FPDF 
import time


root = Tk()
root.geometry("540x400")
root.configure(bg="cyan")
Label(root,text="Hello Buddy! \n Get Ready to Work\n",font='cosmicsansms 20 bold',bg="cyan").grid(row=0,column=1)

# --------------------------------------------------------------------------------------------

def close_window():
    root.destroy()

def display_output(output):
    output_label.config(text=output)


# ---------------------------------------------------------------------------------------------
# from pdf2docx import Converter



def pdfToWord():

    def process(fin,fout):
        filename = fin.get()
        fileoutname = fout.get()
        o_pdf = filename
        n_docx = fileoutname

        obj = Converter(o_pdf)
        obj.convert(n_docx)
        obj.close()

        output = "PDF Converted to Word  Successfully"
        display_output(output)

    # GUI
    root = Tk()
    root.geometry("500x100")
    root.configure(bg="cyan")

    fname = Label(root,text='Input File name: ',bg='cyan',pady=10,padx=10)
    fname.grid(row=1,column=0)

    fnameout = Label(root,text='Output File name: ',bg='cyan',pady=10,padx=10)
    fnameout.grid(row=2,column=0)

    fnameval = StringVar()
    fnameentry = Entry(root,textvariable=fnameval)
    fnameentry.grid(row=1,column=1)

    fnameoutval = StringVar()
    fnameoutentry = Entry(root,textvariable=fnameoutval) 
    fnameoutentry.grid(row=2,column=1)

    Button(text="Submit", command=lambda: process(fnameentry, fnameoutentry), bg="green",fg="white").grid(row=5, column=1)
    root.mainloop()


# -----------------------------------------------------------------------------------------------


def  wordToPdf():

    def process(fin,fout):
        filename = fin.get()
        fileoutname = fout.get()

        o_docx = filename
        n_pdf = fileoutname

        convert(o_docx,n_pdf)
        output = "Word converted to PDF successfully"
        display_output(output)

    # GUI
    root = Tk()
    root.geometry("500x100")
    root.configure(bg="cyan")

    fname = Label(root,text='Input File name: ',bg='cyan',pady=10,padx=10)
    fname.grid(row=1,column=0)

    fnameout = Label(root,text='Output File name: ',bg='cyan',pady=10,padx=10)
    fnameout.grid(row=2,column=0)

    fnameval = StringVar()
    fnameentry = Entry(root,textvariable=fnameval)
    fnameentry.grid(row=1,column=1)

    fnameoutval = StringVar()
    fnameoutentry = Entry(root,textvariable=fnameoutval) 
    fnameoutentry.grid(row=2,column=1)

    Button(text="Submit", command=lambda: process(fnameentry, fnameoutentry), bg="green",fg="white").grid(row=5, column=1)
    root.mainloop()



# -----------------------------------------------------------------------------------------------

def pdf2Img():

    def process():
        o_pdf = convert_from_path(fnameentry.get(),poppler_path=r"C:\Users\divyr\OneDrive\Desktop\poppler-23.11.0\poppler-23.11.0\Library\bin")
        
        # counting pages and cerating images
        
        for i in range(len(o_pdf)):
            o_pdf[i].save("n_"+str(i+1)+".jpg","JPEG")
        
        print("Pdf Converted to images")
    # GUI
    root = Tk()
    root.geometry("500x200")
    root.configure(bg="cyan")

    fname = Label(root,text='Input File name: ',bg='cyan',pady=10,padx=10)
    fname.grid(row=1,column=0)


    fnameval = StringVar()
    fnameentry = Entry(root,textvariable=fnameval)
    fnameentry.grid(row=1,column=1)

   

    Button(text="Submit", command=process, bg="green",fg="white").grid(row=5, column=1)
    root.mainloop()

# -----------------------------------------------------------------------------------------------

def watermark_on_pdf():

    def process():
        filename = fnameentry.get()
        fileoutname = fnamewentry.get()
        # o_pdf = filename
        # n_docx = fileoutname

        o_pdf1 = Pdf.open(filename)
        o_pdf2 = Pdf.open(fileoutname)

        destination_page = Page(o_pdf1.pages[0])
        source_page = Page(o_pdf2.pages[0])

        destination_page.add_overlay(source_page,Rectangle(0,0,150,150))
        o_pdf1.save(fnameoutentry.get())

        # output = "Watermark added successfully"
        # display_output(output)

    # GUI
    root = Tk()
    root.geometry("500x150")
    root.configure(bg="cyan")

    fname = Label(root,text='Input File name: ',bg='cyan',pady=10,padx=10)
    fname.grid(row=1,column=0)

    fnamew = Label(root,text='Input watermark File name: ',bg='cyan',pady=10,padx=10)
    fnamew.grid(row=2,column=0)

    fnameout = Label(root,text='Output File name: ',bg='cyan',pady=10,padx=10)
    fnameout.grid(row=3,column=0)

    fnameval = StringVar()
    fnameentry = Entry(root,textvariable=fnameval)
    fnameentry.grid(row=1,column=1)

    fnamevalw = StringVar()
    fnamewentry = Entry(root,textvariable=fnamevalw)
    fnamewentry.grid(row=2,column=1)

    fnameoutval = StringVar()
    fnameoutentry = Entry(root,textvariable=fnameoutval) 
    fnameoutentry.grid(row=3,column=1)

    Button(text="Submit", command= process, bg="green",fg="white").grid(row=5, column=1)
    root.mainloop()

# --------------------------------------------------------------------------------------------------


def basicCalculator():
    print("Calculator Opened")
    def on_button_click(event):
        # Get the button text
        text = event.widget.cget("text")
        # Perform calculation based on the button clicked
        if text == "=":  # If the button clicked is "=", perform calculation
            try:
                result = eval(entry.get())  # Evaluate the expression in the entry widget
                # formatted_result = "{:.2f}".format(result)
                entry.delete(0, END)  # Delete the current content in the entry widget
                entry.insert(END, result)  # Insert the result into the entry widget / result(formatted_result)
            except Exception as e:  # Handle exceptions such as division by zero
                entry.delete(0, END)  # Delete the current content in the entry widget
                entry.insert(END, "Error")  # Display error message
        elif text == "C":  # If the button clicked is "C", clear the entry widget
            entry.delete(0, END)  # Delete the current content in the entry widget
        else:  # If a digit or operator button is clicked, add it to the entry widget
            entry.insert(END, text)  # Insert the button text into the entry widget
    
    # Create the main window
    root = Tk()  # Create an instance of the Tk class
    root.title("Basic Calculator")  # Set the title of the window
    
    # Create entry widget for displaying input and output
    entry = Entry(root, width=25, font=('Arial', 14))  # Create an entry widget
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
        button = Button(root, text=button_label, width=5, height=2, font=('Arial', 12))  # Create a button
        button.grid(row=row, column=col)  # Place the button in the grid
        col += 1  # Move to the next column
        if col > 3:  # If the column exceeds 4, reset it to 0 and move to the next row
            col = 0
            row += 1
    
    # Bind button clicks to the function
    root.bind("<Button-1>", on_button_click)  # Bind left mouse button click event to on_button_click function
    
    # Run the main event loop
    root.mainloop()  # Start the event loop to display the GUI and handle user interactions

    output = "Calculator Opened Successfully"
    




def stopWatch():
    
    class Timer:
        def __init__(self, root):
            self.root = root  # Store the root window reference
            self.root.title("Timer")  # Set the title of the root window
    
            self.running = False  # Flag to track if the timer is running or not
            self.start_time = None  # Variable to store the start time of the timer
            self.elapsed_time = 0  # Variable to store the elapsed time
    
            # Create a label to display the time
            self.label = Label(root, text="00:00:00", font=("Arial", 24))
            self.label.pack(pady=10)  # Place the label in the window with some padding
    
            # Create a button to start the timer
            self.start_button = Button(root, text="Start", command=self.start_timer)
            self.start_button.pack(side=LEFT, padx=10)  # Place the button on the left side with padding
    
            # Create a button to stop the timer
            self.stop_button = Button(root, text="Stop", command=self.stop_timer)
            self.stop_button.pack(side=LEFT, padx=10)  # Place the button on the left side with padding
            self.stop_button.config(state=DISABLED)  # Initially disable the stop button
    
            # Create a button to reset the timer
            self.reset_button = Button(root, text="Reset", command=self.reset_timer)
            self.reset_button.pack(side=RIGHT, padx=10)  # Place the button on the right side with padding
    
            # Initialize the timer display
            self.update_time()
    
        def start_timer(self):
            if not self.running:  # If the timer is not running
                self.running = True  # Set the running flag to True
                self.start_time = time.time() - self.elapsed_time  # Record the start time
                self.start_button.config(state=DISABLED)  # Disable the start button
                self.stop_button.config(state=NORMAL)  # Enable the stop button
                self.update_time()  # Update the time display
    
        def stop_timer(self):
            if self.running:  # If the timer is running
                self.running = False  # Set the running flag to False
                self.start_button.config(state=NORMAL)  # Enable the start button
                self.stop_button.config(state=DISABLED)  # Disable the stop button
    
        def reset_timer(self):
            self.running = False  # Set the running flag to False
            self.start_button.config(state=NORMAL)  # Enable the start button
            self.stop_button.config(state=DISABLED)  # Disable the stop button
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
    root = Tk()
    # Create an instance of the Timer class with the root window as an argument
    timer = Timer(root)
    # Start the Tkinter event loop
    root.mainloop()
    




def image2Pdf():

    def process():
        pdf = FPDF()  # Creating an instance of the FPDF class to work with PDFs
        pdf.set_auto_page_break(0)  # Disabling auto page break to manually control page breaks

        # Creating a list to store the names of all images in a folder
        # Note: You can also ask the user to input the path where images are located
        img_list = [x for x in os.listdir(fnameentry.get())]
    
        # Iterating through each image in the list
        for img in img_list:
            pdf.add_page()  # Adding a new page to the PDF for each image
            image = fnameentry.get()+"\\" + img  # Constructing the path of the image file
            pdf.image(image)  # Adding the image to the PDF page
    
        pdf.output("imagesCon.pdf")  # Saving the PDF with all images added
        print("Successfully converted")  # Printing a success message after PDF creation
    
        # output = "Images converted to Pdf successfully"
        # display_output(output)
    # GUI
    root = Tk()
    root.geometry("500x200")
    root.configure(bg="cyan")

    fname = Label(root,text='Input File name: ',bg='cyan',pady=10,padx=10)
    fname.grid(row=1,column=0)


    fnameval = StringVar()
    fnameentry = Entry(root,textvariable=fnameval)
    fnameentry.grid(row=1,column=1)

   

    Button(text="Submit", command=process, bg="green",fg="white").grid(row=5, column=1)
    root.mainloop()



def digitalClock():
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

    output = "Digital Clock Opened Successfully"
    display_output(output)


Button(text="PDF >> WORD", command=pdfToWord, borderwidth=2, highlightbackground='black', highlightcolor='black', font=('Helvetica', 10, 'bold')).grid(row=1, column=0, padx=10, pady=10)
Button(text="WORD >> PDF", command=wordToPdf, borderwidth=2, highlightbackground='black', highlightcolor='black', font=('Helvetica', 10, 'bold')).grid(row=1, column=1, padx=10, pady=10)
Button(text="PDF >> IMAGE", command=pdf2Img, borderwidth=2, highlightbackground='black', highlightcolor='black', font=('Helvetica', 10, 'bold')).grid(row=1, column=2, padx=10, pady=10)
Button(text="WATERMARK", command=watermark_on_pdf, borderwidth=2, highlightbackground='black', highlightcolor='black', font=('Helvetica', 10, 'bold')).grid(row=3, column=0, padx=10, pady=10)
Button(text="IMAGE >> PDF", command=image2Pdf, borderwidth=2, highlightbackground='black', highlightcolor='black', font=('Helvetica', 10, 'bold')).grid(row=3, column=2, padx=10, pady=10)
Button(text="CALCULATOR", command=basicCalculator, borderwidth=2, highlightbackground='black', highlightcolor='black', font=('Helvetica', 10, 'bold')).grid(row=5, column=2, padx=10, pady=10)
Button(text="STOPWATCH", command=stopWatch, borderwidth=2, highlightbackground='black', highlightcolor='black', font=('Helvetica', 10, 'bold')).grid(row=3, column=1, padx=10, pady=10)
Button(text="DIGITAL CLOCK", command=digitalClock, borderwidth=2, highlightbackground='black', highlightcolor='black', font=('Helvetica', 10, 'bold')).grid(row=5, column=0, padx=10, pady=10)
# Button(text="HANDWRITTEN", command=textToHandwritten, borderwidth=2, highlightbackground='black', highlightcolor='black', font=('Helvetica', 10, 'bold')).grid(row=5, column=1, padx=10, pady=10)

output_label = Label(root, text="", bg="cyan", fg="black", font='cosmicsansms 12')
output_label.grid(row=6, column=1)
Button(root, text="Close", command=close_window, borderwidth=2, highlightbackground='black', highlightcolor='black',bg="red", fg="white", font=('Helvetica', 10, 'bold')).grid(row=7, column=1, pady=10)


root.mainloop()