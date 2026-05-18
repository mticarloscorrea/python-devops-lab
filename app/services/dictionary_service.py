class Dictionary:
    def __init__(self):
        self.entries = {}

    def newentry(self, word, definition):
        self.entries[word] = definition

    def look(self,word):
        if word in self.entries:
            return self.entries[word]
        else:
            return "Can't find entry for {}".format(word)   

