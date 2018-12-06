"""This class holds the methods for the Scanner object, which will scan through a given text string and sort it into a 2D list, tracking
    unique instances of each word and tallying how many of each there are."""


class Scanner:
    """Data initially starts with 1 void entry, but at the end of the scan, this entry is removed from the list. This is so the for loop runs at least once"""
    data = [['', 0]]
    count = 0

    """Primary function to scan through document and store results in local list 'data'"""
    def scan(self, text):
        global index
        """For each word in the text:"""
        for x in text.split():
            """Uncomment the following block of code to enable verbose output"""
            """print(self.count)
            self.count += 1"""
            in_list = False
            """Check if that word is in the list already:"""
            for i in range(len(self.data)):
                if x in self.data[i]:
                    in_list = True
                    index = i
            """If word exists in list, increment its current count by 1"""
            """Otherwise, add that word to the list, and give it a count of 1"""
            if in_list:
                self.data[index][1] += 1
            else:
                self.data.append([x, 1])
        """Remove the void list entry"""
        if self.data[0][0] == '':
            self.data.pop(0)

        """calls the sort function on the populated list"""
        self.sort_data()

    """Sorts the list using the 2 value in each sublist. The lambda function is necessary to do this."""
    def sort_data(self):
        self.data.sort(key=lambda x: x[1], reverse=True)

    """Prints each entry in the list"""
    def output(self):
        for entry in self.data:
            print(entry)

    """Calculates and appends each words appearance percent to its entry in the list"""
    def append_percents(self):
        for i in range(len(self.data)):
            percent = (self.data[i][1] / len(self.data)) * 100
            percent = format(percent, '.2f') + '%'
            self.data[i].append(percent)


