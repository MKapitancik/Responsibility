from DataPreparation import TextNormalization
from DataPreparation import TeamNameParser

class DataCleaning:
    def __init__(self, text_normalization : TextNormalization, team_parser : TeamNameParser):
        self.txt_norm = text_normalization
        self.team_p = team_parser
    
    def Clean(self, data):
        result = []

        for row in data:
            story = row[0]
            text = self.txt_norm.Normalize(row[1])            
            team = self.team_p.Parse(self.txt_norm.Normalize(row[2]))

            if (team):
                result.append([story, text, team])

        return result
