class Scanner:
    list = []

    def scan(self, text):
        for x in text.lower().split():
            for i in range(len(self.list)):
                if x == self.list[i][0]:
                    self.list[i][0] += 1
                elif x != self.list[i][0]:
                    self.list.append([x, 1])
