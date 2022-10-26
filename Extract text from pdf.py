import PyPDF2
pdf = open("Naveen.pdf", "rb")
reader = PyPDF2.PdfFileReader(pdf)
page = reader.getPage(0)
print(page.extractText())
