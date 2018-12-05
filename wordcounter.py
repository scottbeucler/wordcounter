from document import Document
from scanner import Scanner

my_doc = Document('moon.txt')
scanner = Scanner()

scanner.scan(my_doc.text)
