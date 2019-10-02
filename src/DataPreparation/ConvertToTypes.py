class ConvertToTypes:
    def __init__(self, *types):
        self.types = types

    def Convert(self, data):
        converted = []
        for d in data:
            line = []
            for i, type in enumerate(self.types):
                if(type == None):
                    continue
                line.append(type(d[i]))
            converted.append(line)

        return converted