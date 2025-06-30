from docx import Document


text = input("Enter text to convert to DOCX: ")



doc = Document()
doc.add_paragraph(text)
doc.save("hello_world.docx")
print("DOCX file created successfully.")