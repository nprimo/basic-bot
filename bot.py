import discord


def hello(message: discord.Message, av: list[str]) -> str:
    print(f'received the following arguments: {av}')
    return f'Hello {message.author.mention}'


def commands(key: str, message: discord.Message, av: list[str]) -> str:
    commands = {
        # help -> show all the commands options
        'hello': hello,
        # additional commands
    }
    command_to_exec = commands.get(key[1:])
    if command_to_exec:
        return command_to_exec(message, av)
    return 'Unknown command'
