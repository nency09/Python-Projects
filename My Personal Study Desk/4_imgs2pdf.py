from fpdf import FPDF  # Importing FPDF library for PDF generation
import os  # Importing os module for interacting with the operating system

pdf = FPDF()  # Creating an instance of the FPDF class to work with PDFs
pdf.set_auto_page_break(0)  # Disabling auto page break to manually control page breaks

# Creating a list to store the names of all images in a folder
# Note: You can also ask the user to input the path where images are located
img_list = [x for x in os.listdir("Imagesss")]

# Iterating through each image in the list
for img in img_list:
    pdf.add_page()  # Adding a new page to the PDF for each image
    image = "Imagesss\\" + img  # Constructing the path of the image file
    pdf.image(image)  # Adding the image to the PDF page

pdf.output("imagesCon.pdf")  # Saving the PDF with all images added
print("Successfully converted")  # Printing a success message after PDF creation
