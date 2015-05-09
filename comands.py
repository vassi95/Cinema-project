class Commands:

    all_commands = {}

    @classmethod
    def add_commands(cls, new_command, func):
        cls.all_commands[new_command] = func
        return func

    @classmethod
    def run(cls, enter):
        enter = enter.split(" ")
        new_command = enter[0]
        arguments = enter[1:]
        if new_command in cls.all_commands:
                cls.all_commands[new_command](*arguments)
        else:
            print('No such command,see the available ones in help!')
