import sys


def calculate_command(definitions, terms):
    expression = ''
    for term in terms:
        if term != '+' and term != '-' and term != '=':
            if definitions.get(term) is not None:
                expression += definitions.get(term)
            else:
                return 'unknown'
        else:
            expression += term

    total = str(eval(expression[:-1]))
    inverted_definitions = {v: k for k, v in definitions.items()}
    if inverted_definitions.get(total) is None:
        return 'unknown'
    else:
        return inverted_definitions.get(total)


if __name__ == '__main__':
    definitions = {}

    for command in sys.stdin.readlines():
        command_components = command.split()
        if command_components[0] == 'def':
            definitions[command_components[1]] = command_components[2]
        elif command_components[0] == 'calc':
            calculated_value = calculate_command(definitions, command_components[1:])
            print('{} = {}'.format(command[5:-2], calculated_value))
        elif command_components[0] == 'clear':
            definitions = {}
