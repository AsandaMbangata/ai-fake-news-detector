
import copy

class Article:
    def __init__(self, text):
        self.text = text

    def clone(self):
        return copy.deepcopy(self)