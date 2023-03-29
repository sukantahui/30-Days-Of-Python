from pdf2docx import Converter
import easygui
pdf_file = "python-lists.pdf"
doc_file = "python-lists.docx"


path = easygui.fileopenbox()
print(path)

cv=Converter(path)
cv.convert(doc_file)
cv.close()