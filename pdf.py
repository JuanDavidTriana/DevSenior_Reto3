#pip install pymupdf
#https://wkhtmltopdf.org/downloads.html

import pdfkit

path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

pdfkit.from_file("archivo.html", "salida.pdf", configuration=config)
