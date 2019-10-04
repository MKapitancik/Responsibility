class TeamNameParser:
    def __init__(self):
        self.teams = set([
            'red',
            'jerry',
            'sid',
            'jago',
            'trinity',
            'morpheus',
            'neo',
            'mercury',
        ])

    def Parse(self, text):
        match = next((team for team in self.teams if team in text), None)
        return match

