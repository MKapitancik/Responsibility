import re

class CommitParser:
    """Use to parse the single commit
    """
    def __init__(self):
        self.p = re.compile(r"(\s(?P<story>\d{3,})\s-\s(?P<text>.*)\s\(#(?P<pullrequest>\d*))")

    def Parse(self, line):
        """Line to be parsed into categories

        Returns: None if match is not found, othervide array of values in order [story, text, PR]
        """
        m = self.p.search(line)
        if (m):
            return [int(m.group('story')), m.group('text'), int(m.group('pullrequest'))]
        else:
            return None