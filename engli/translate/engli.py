import re
import argparse
import os
from commandsmap import commandmap

code_map = commandmap


def execute_command(command_template):
    match = re.findall("{(.*?)}", command_template)
    variables = {}
    for variable in match:
        variables[variable] = input(f"Enter value for variable {variable}: ")
    command_interpolated = command_template.format(**variables)
    os.system(command_interpolated)


def command_line_arg(arguments=None):
    parser = argparse.ArgumentParser(description='Command in your code_map')
    parser.add_argument('command', help='command')
    if arguments:
        return vars(parser.parse_args(arguments))
    return vars(parser.parse_args())


if __name__ == "__main__":
    args = command_line_arg()
    command = args.get("command")
    if command in code_map:
        execute_command(code_map[command])
    else:
        print(f"No command matched with '{command}'")