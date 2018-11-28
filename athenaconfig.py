from athenacommand import AthenaCommand
from json_converter import JsonConvert

@JsonConvert.register
class AthenaConfiguration():

    def __init__(self, **entries):
        self.commands = []
        self.__dict__.update(entries)

    def __str__(self):
        s = '[\n'
        for command in self.commands:
            s += command.__str__() + ',\n'
        s += ']'
        return s