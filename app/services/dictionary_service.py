"""Dictionary service."""
class Dictionary:
    """Dictionary operations."""
    def __init__(self):
        """Initialize dictionary."""
        self.entries = {}

    def newentry(self, word, definition):
        """Add new dictionary entry."""
        self.entries[word] = definition

    def look(self,word):
        """Search dictionary entry."""
        if word in self.entries:
            return self.entries[word]
        else:
            return "Can't find entry for {}".format(word)   

