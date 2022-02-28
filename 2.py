from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen.canvas import Canvas

page_to_merge = 0 #Refers to the First page of PDF 
xcoor = 123 #To be changed according to your pdf
ycoor = 697

input_pdf = PdfFileReader(open('/home/rahul/Downloads/Fill_pdf.pdf', "rb"))
page_count = input_pdf.getNumPages()
inputpdf_page_to_be_merged = input_pdf.getPage(page_to_merge)

packet = io.BytesIO()
c = Canvas(packet,pagesize=(inputpdf_page_to_be_merged.mediaBox.getWidth(),inputpdf_page_to_be_merged.mediaBox.getHeight()))
c.drawString(xcoor,ycoor,"Hello World")
c.drawString(123,757,"Hello World")
c.save()
packet.seek(0)

overlay_pdf = PdfFileReader(packet)
overlay = overlay_pdf.getPage(0)

output = PdfFileWriter()

for PAGE in range(page_count):
    if PAGE == page_to_merge:
        inputpdf_page_to_be_merged.mergeRotatedTranslatedPage(overlay, 
                inputpdf_page_to_be_merged.get('/Rotate') or 0, 
                overlay.mediaBox.getWidth()/2, overlay.mediaBox.getWidth()/2)
        output.addPage(inputpdf_page_to_be_merged)
    
    else:
        Page_in_pdf = input_pdf.getPage(PAGE)
        output.addPage(Page_in_pdf)

outputStream = open("/home/rahul/Visualstudio/hh.pdf", "wb")
output.write(outputStream)
outputStream.close()