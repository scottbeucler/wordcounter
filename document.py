class Document(object):
    def __init__(self, file):
        self.file = file
        with open(self.file) as file:
            self.text = file.read()
