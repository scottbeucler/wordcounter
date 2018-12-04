class Document:
    def __init__(self, file):
        document = open(file, 'r')
        text = document.read()
