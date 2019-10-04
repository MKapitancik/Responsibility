import re

class TextNormalization():
    """Converts text to lower and remove special characters
    """
    def SetStrategy(self, *operations):
        self.operations = operations

    def Normalize(self, text : str):
        if (len(self.operations) == 0):
            raise NotImplementedError()
        for o in self.operations:
            text = o(text)

        return text	