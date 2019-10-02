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
                value = o(row[c])
                if (value is not None):
                    line.append(value)

            if len(line) == len(self.columnOperations.keys()):
                result.append(line)

        return result
