import fpdf

text= input("Enter text to convert to PDF: ")

pdf = fpdf.FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt=text, ln=True, align='C')
pdf.output("hello_world.pdf")
