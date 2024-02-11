import re
import argparse
import os
from commandsmap import commandmap
from fuzzywuzzy import process

# Make the dictionary keys case-insensitive
code_map = {k.lower(): v for k, v in commandmap.items()}

def execute_command(command_template):
    match = re.findall("{(.*?)}", command_template)
    variables = {}
    for variable in match:
        variables[variable.lower()] = input(f"Enter value for variable {variable}: ")
    command_interpolated = command_template.format(**variables)
    os.system(command_interpolated)

def command_line_arg(arguments=None):
    parser = argparse.ArgumentParser(description='Command in your commandmap')
    parser.add_argument('command', help='command')
    if arguments:
        return vars(parser.parse_args(arguments))
    return vars(parser.parse_args())

def get_closest_map(command, code_map):
    best_match = process.extractOne(command, code_map.keys())
    return best_match

if __name__ == "__main__":
    args = command_line_arg()
    command = args.get("command").lower()

    closest_command = get_closest_map(command, code_map)

    if closest_command:
        if closest_command[1] < 90:  # You can adjust the matching score threshold.
            print(f"Your command did not closely match any known commands. Maybe you meant '{closest_command[0]}'?")
        else:
            execute_command(code_map[closest_command[0]])
    else:
        print(f"No command matched with '{command}'")