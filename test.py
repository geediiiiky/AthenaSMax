from athena_config import AthenaConfiguration
from athena_command import AthenaCommand
from athena_command import CommandParameter
from json_converter import JsonConvert


aconfig = JsonConvert.FromFile('testconfig.json')
print aconfig

# aconfig = AthenaConfiguration()
# command = AthenaCommand()
# parameter = CommandParameter()
# command.parameters['ParamA'] = parameter
# aconfig.commands.append(command)
# print JsonConvert.ToJSON(aconfig)