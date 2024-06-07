from pdf2image import convert_from_path

o_pdf = convert_from_path("Grow By Little Content Writer.pdf",poppler_path=r"D:\CLG\SEM-3\Projects\poppler-23.11.0\Library\bin")

# counting pages and cerating images

for i in range(len(o_pdf)):
    o_pdf[i].save("n_"+str(i+1)+".jpg","JPEG")

print("Pdf Converted to images")