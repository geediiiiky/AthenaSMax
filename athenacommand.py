import json
from enum import Enum
from json_converter import JsonConvert


class CommandType(str, Enum):
    ScriptCommand = 'ScriptCommand'   # a script (.bat, .cmd on windows, .sh, .command on mac, etc.)
    InlineCommand = 'InlineCommand'   # a simple command such as "git pull"
    InternalFunction = 'InternalFunction'    # an internal function in this project


class ParameterType(str, Enum):
    Mandatory = 'Mandatory'   # hidden parameter
    OneOf = 'OneOf'       # radio buttons
    OnOff = 'OnOff'       # checkbox

@JsonConvert.register
class AthenaCommand():
    
    def __init__(self, **entries):
        self.disabled = False
        self.caption = "My Command"
        self.groupName = "My Group"
        self.tabName = "My Tab"
        self.type = CommandType.ScriptCommand
        self.commandStr = ""
        self.hotKey = ""
        self.tooltip = "command tooltip"
        self.startNoConsoleWindow = False
        self.isFavorite = False
        self.parameters = {}
        # update with entries
        self.__dict__.update(entries)
        self.type = CommandType(self.type)

    def __str__(self):
        return '{}'.format(self.tabName + '/' + self.groupName + '/' + self.caption)

@JsonConvert.register
class CommandParameter():

    def __init__(self, **entries):
        self.selectedIndex = 0
        self.displayName = "Parameter"
        self.type = ParameterType.OneOf
        self.collection = []
        self.__dict__.update(entries)
        self.type = ParameterType(self.type)
