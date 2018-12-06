"""This class holds the file to be read by the scanner, and sanitizes the input by removing special characters, leaving just words."""


class Document(object):
    bad_chars = ['.', ',', '\'', '!', '\"', '?', '[', ']', '(', ')', '{', '}', 'â¹', '$', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ':', ';']

    """Initialization method"""
    def __init__(self, file):
        self.file = file
        with open(self.file) as file:
            self.text = file.read().lower()
        self.sanitize()

    """This method removes any characters from the extracted text that mach the 'bad chars' list of characters."""
    def sanitize(self):
        for x in self.bad_chars:
            self.text = self.text.replace(x, '')
        self.text = self.text.replace('--', ' ')
