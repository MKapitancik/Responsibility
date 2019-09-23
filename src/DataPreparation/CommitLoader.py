import re
from DataPreparation.CommitParser import CommitParser

class CommitLoader:
    def __init__(self, path, parser : CommitParser):
        self.path = path
        self.parser = parser        

    def Load(self):
        data = []
        with open(self.path, 'r', encoding="utf8") as f:
            for line in f.readlines():
                parsed = self.parser.Parse(line.strip())
                if (parsed):
                    data.append(parsed)
        return data
                