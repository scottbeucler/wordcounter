"""This class holds the file to be read by the scanner, and sanitizes the input by removing special characters, leaving just words."""


class Document(object):
    bad_chars = ['.', ',', '\'', '!', '\"', '?', '[', ']', '(', ')', '{', '}', 'â¹', '$', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ':', ';', '“', '”', '°', '‘', '’']

    """Initialization method"""
    """Uses two private functions to prompt a user for a file path, and sanitizes the text extracted from the file, while opening and reading the file in between those steps"""
    def __init__(self):
        self.file = self.__prompt_for_file()
        with open(self.file, encoding="utf8") as file:
            self.text = file.read().lower()
        self.__sanitize()

    """This private method removes any characters from the extracted text that mach the 'bad chars' list of characters."""
    def __sanitize(self):
        for x in self.bad_chars:
            self.text = self.text.replace(x, '')
        self.text = self.text.replace('--', ' ')

    """This private method asks for users to give the path for a text file. If a file other than a text file is given, the user is re-prompted"""
    def __prompt_for_file(self):
        file_path = None
        print("Enter a filename/path of a text file to be analyzed: ")
        text_file = False
        while not text_file:
            file_path = input()
            if file_path.endswith('.txt'):
                text_file = True
            else:
                print("Input a text file!")
        return file_path

    """This method returns the word count of the sanitized and split string"""
    def get_word_count(self):
        return len(self.text.split())
