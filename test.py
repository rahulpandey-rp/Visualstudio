from fpdf import FPDF
class PDF(FPDF):
    def titles(self):
        self.set_xy(0.0,0.0)
        self.set_font('Arial', 'B', 16)
        self.set_text_color(220, 50, 50)
        self.cell(w=72, h=676, align='C', txt="LORD OF THE PDFS", border=0)

pdf = PDF(orientation='P', unit='pt', format='A4')
pdf.add_page()
pdf.titles()
pdf.output('/home/rahul/Visualstudio/hh.pdf','F')
