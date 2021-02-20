import discord
from discord.ext import commands

from bot.config import settings, gifs


class Error(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        desc = f'''Команда: **{ctx.message.content.split()[0][len(settings['PREFIX']):]}**
Отправитель: {ctx.author.mention}

Ошибка: '''
        if isinstance(error, commands.NotOwner):
            desc += 'Пользователь не является создателем бота'
        elif isinstance(error, commands.MissingPermissions):
            desc += 'Недостаточно прав'
        elif isinstance(error, commands.MissingRequiredArgument):
            desc += 'Пропущен аргумент'
        elif isinstance(error, commands.BadArgument):
            desc += 'Неправильное использование команды'
        else:
            desc += f'{error}'

        colour = discord.Colour.from_rgb(255, 30, 30)

        emb = discord.Embed(title='Ошибка', description=desc, colour=colour)
        emb.set_thumbnail(url=gifs['ERROR'])

        await ctx.send(embed=emb)


def setup(client):
    client.add_cog(Error(client))