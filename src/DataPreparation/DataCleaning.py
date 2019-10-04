from DataPreparation import TextNormalization
from DataPreparation import TeamNameParser

class DataCleaning:
    def __init__(self, columnOperations : dict):
        self.columnOperations = columnOperations
    
    def Clean(self, data):
        result = []    
        for row in data:
            line = []
            for c, o in self.columnOperations.items():
                if o is None:
                    line.append(row[c])  
                    continue            
                value = self.ParseRow(o, row[c])
                if (value):
                    line.append(value)

            if len(line) == len(self.columnOperations.keys()):
                result.append(line)               
        return result

    def ParseRow(self, operations, row):
        sentence = ''
        for word in row.split():
            parsed = operations(word)
            if(parsed):
                sentence += parsed + ' '

        return sentence[:-1]