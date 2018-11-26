import json
from enum import Enum

class CommandType(Enum):
    ScriptCommand = 1   # a script (.bat, .cmd on windows, .sh, .command on mac, etc.)
    InlineCommand = 2   # a simple command such as "git pull"
    InternalFunction = 3    # an internal function in this project


class ParameterType(Enum):
    Mandatory = 1   # hidden parameter
    OneOf = 2       # radio buttons
    OnOff = 3       # checkbox

class AthenaCommand():
    
    def __init__(self):
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

    @classmethod
    def from_dict(cls, config):
        command = cls()
        command.__dict__.update(config)
        if command.parameters is not None:
            for k in command.parameters:
                command.parameters[k] = CommandParameter(**command.parameters[k])
        return command


class CommandParameter():

    def __init__(self, **entries):
        self.selectedIndex = 0
        self.displayName = "Parameter"
        self.type = ParameterType.OneOf
        self.collection = {}
        self.__dict__.update(entries)
