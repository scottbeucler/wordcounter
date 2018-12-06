class Scanner:
    data = [['', 0]]

    def scan(self, text):
        global index
        for x in text.split():
            in_list = False
            for i in range(len(self.data)):
                if x in self.data[i]:
                    in_list = True
                    index = i
            if in_list:
                self.data[index][1] += 1
            else:
                self.data.append([x, 1])
        self.data.pop(0)
        self.sort_data()

    def print_text(self, text):
        for x in text.split():
            print(x)

    def sort_data(self):
        self.data.sort(key=lambda x: x[1], reverse=True)

    def output(self):
        for entry in self.data:
            print(entry)
