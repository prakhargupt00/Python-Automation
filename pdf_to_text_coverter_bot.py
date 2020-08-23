# coverts pdf file to text file 

# PDFMiner  is a tool for extracting information from the  pdf into various formats such as HTML,tagged-PDF etc

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# PDFResourceManager is used to store shared resources of a pdf such as fonts, images etc.

# PDFPageInterpreter is used to process the page contents

from pdfminer.pdfpage import PDFPage
# PDFPage is used to create an object that holds the information about an image

from pdfminer.converter import TextConverter, HTMLConverter, XMLConverter
# TextConverter is used to convert any PDF to text.It is given to PageInterpreter object

from pdfminer.layout import LAParams
# LAParams takes care about the layout of the pdf file 

import io

# path to your pdf file
pdf_path='D:\\test_1.pdf'
pdf=open(pdf_path,'rb')
in_memory_stream=io.StringIO()

lp = LAParams()
resource_manager_object = PDFResourceManager()
converter_object = TextConverter(resource_manager_object, in_memory_stream, laparams=lp)
interpreter_object = PDFPageInterpreter(resource_manager_object,converter_object)

#interpret to text for each page 
pages = PDFPage.get_pages(pdf)

for page in pages:
    interpreter_object.process_page(page)
    #save it
    text = in_memory_stream.getvalue()

result_file  = open("D:\\test_result.txt","wb")
result_file.write(text.encode('utf-8'))

print("Conversion Complete !!")




