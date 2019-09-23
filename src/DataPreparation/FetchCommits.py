import csv

class FetchCommits:
    def __init__(self, readfunction,  path, mode, encoding, delimiter):
        self.readfunction = readfunction
        self.path = path
        self.mode = mode
        self.encoding = encoding
        self.delimiter = delimiter

    def Load(self):
        data = []
        with self.readfunction(self.path, mode=self.mode, encoding=self.encoding) as f:
            csv_reader = csv.reader(f, delimiter=self.delimiter)

            for i, row in enumerate(csv_reader):
                if(i == 0):
                    continue
                                
                data.append([int(row[0]), str(row[1]), str(row[3])])
        return data
                