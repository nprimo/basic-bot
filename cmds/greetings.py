from discord.ext import commands


@commands.group()
async def greetings(ctx):
    if ctx.invoked_subcomand is None:
        await ctx.send(f"No, {ctx.subcommand_passed} does not belong here!")


@greetings.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author}")


async def setup(bot):
    # bot.add_command(greetings) # to add group of commands
    bot.add_command(hello)
