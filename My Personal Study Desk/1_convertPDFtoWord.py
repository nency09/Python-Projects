from pdf2docx import Converter

o_pdf = "PLSQL- coursera -uni of michi.pdf"
n_docx = "new5.docx"

obj = Converter(o_pdf)
obj.convert(n_docx)
obj.close()