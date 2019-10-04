import re

class TextOperations:
    def __init__(self):
        self.single_whitespace_p = re.compile(r'\s\s+')
        self.strip_ends_p = re.compile(r'^\s+|\s+$')
        self.only_words_p = re.compile('[^a-zA-Z0-9 ]') # filter for A-Z and numbers

    def ToLower(self, text):
        return text.lower()

    def OnlyCharacters(self, text):
        return self.only_words_p.sub('', text)

    def SingleWhitespaces(self, text):
        return self.single_whitespace_p.sub(' ', text)

    def StripEndWhitespaces(self, text):
        return self.strip_ends_p.sub('', text)

    def RemoveCamelCase(self, text):
        result = ''
        for w in text.split(' '):
            c2 = None
            for c1, c2 in zip(w, w[1:]):
                result += c1
                if (c2.isupper() and c1.islower()):
                    result += ' '
            if (c2):
                result += c2
            result += ' '

        return result[:-1]