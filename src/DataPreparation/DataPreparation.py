from random import shuffle

from DataPreparation.FetchCommits import FetchCommits
from DataPreparation.TextNormalization import TextNormalization
from DataPreparation.TeamNameParser import TeamNameParser
from DataPreparation.DataCleaning import DataCleaning
from DataPreparation.ConvertToTypes import ConvertToTypes
from DataPreparation.TextOperations import TextOperations

class DataPreparation:
    def __init__(self, fileName, readMode, encoding, separator):
        self.fileName = fileName
        self.readMode = readMode
        self.encoding = encoding
        self.separator = separator

    def GetData(self):
        commits = FetchCommits(open, self.fileName, self.readMode, self.encoding, self.separator)
        data = commits.Load()

        typeConverter = ConvertToTypes(int, str, str)
        data = [typeConverter.Convert(row) for row in data]
        shuffle(data)

        to = TextOperations()
        storyOperations = TextNormalization()
        storyOperations.SetStrategy(to.OnlyCharacters, to.RemoveCamelCase, to.SingleWhitespaces, to.StripEndWhitespaces, to.ToLower)

        teamOperations = TextNormalization()
        teamOperations.SetStrategy(to.OnlyCharacters, to.SingleWhitespaces, to.ToLower, TeamNameParser().Parse)

        column_operations = {
            0 : None,
            1 : storyOperations.Normalize,
            2 : teamOperations.Normalize,
        }

        dc = DataCleaning(column_operations)
        data = [row for row in (dc.Clean(d) for d in data) if row is not None]

        return data