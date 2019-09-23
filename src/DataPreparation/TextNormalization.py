import re

class TextNormalization():
    """Converts text to lower and remove special characters
    """
    def __init__(self, operations):
        self.operations = operations

    def Normalize(self, text : str):
        for o in self.operations:
            text = o(text)

        return text	