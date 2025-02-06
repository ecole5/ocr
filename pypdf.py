#Install dependency in project workspace
%pip install PyPDF2


#import package
from PyPDF2 import PdfReader

reader = PdfReader("Samples/text.pdf")
page = reader.pages[0]


print(page.extract_text())

