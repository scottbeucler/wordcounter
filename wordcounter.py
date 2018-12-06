from document import Document
from scanner import Scanner

print("Enter a filename/path of a text file to be analyzed: ")
filename = input()

my_doc = Document(filename)
scanner = Scanner()

scanner.scan(my_doc.text)
scanner.output()