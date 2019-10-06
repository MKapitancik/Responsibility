class ConvertToTypes:
    def __init__(self, *types):
        self.types = types

    def Convert(self, data):
        converted = []
        for i, type in enumerate(self.types):
            if(type == None):
                continue
            converted.append(type(data[i]))

        return converted
