from DataPreparation import TextNormalization
from DataPreparation import TeamNameParser
from nltk.tokenize import word_tokenize
import nltk

class DataCleaning:
    def __init__(self, columnOperations : dict):
        self.columnOperations = columnOperations
    
    def Clean(self, data):
        line = []
        for c, o in self.columnOperations.items():
            if o is None:
                line.append(data[c])  
                continue
            value = self.ParseRow(o, data[c])
            if (value):
                line.append(value)

        if len(line) == len(self.columnOperations.keys()):
            return line               
        return None

    def ParseRow(self, operations, row):
        words = []
        for word in word_tokenize(row):
            parsed = operations(word)
            if(parsed):
                words.append(parsed)

        return ' '.join(words)