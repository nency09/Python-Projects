from pikepdf import Pdf,Page,Rectangle

o_pdf1 = Pdf.open("2_new.pdf")
o_pdf2 = Pdf.open("certi.pdf")

destination_page = Page(o_pdf1.pages[0])
source_page = Page(o_pdf2.pages[0])

destination_page.add_overlay(source_page,Rectangle(0,0,150,150))
o_pdf1.save("new_waterPDF_NEW.pdf")