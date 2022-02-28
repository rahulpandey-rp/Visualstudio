import fitz

### READ IN PDF
doc = fitz.open("/home/rahul/Downloads/Fill_pdf.pdf")

for page in doc:
    ### SEARCH
    text = "Name:"
    text_instances = page.search_for(text)
    print(text_instances)
    ### HIGHLIGHT
    for inst in text_instances:
        highlight = page.add_highlight_annot(inst)
        highlight.update()


### OUTPUT
doc.save("/home/rahul/Visualstudio/hh.pdf", garbage=4, deflate=True, clean=True)