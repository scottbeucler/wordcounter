from document import Document
from scanner import Scanner


def print_text(text):
    """This function accepts a large string as input and prints each individual word"""
    for x in text.split():
        print(x)


my_doc = Document()
scanner = Scanner()

scanner.scan(my_doc.text)
scanner.append_percents()
scanner.output()
# print_text(my_doc.text)

print(my_doc.get_word_count())

output = open("output.txt", 'w', encoding='utf8')
for entry in scanner.data:
    output.write(str(entry) + '\n')
