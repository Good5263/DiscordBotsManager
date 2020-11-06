import discord
from discord.ext import commands

from content.bot.config import gifs


class Clear(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount+1)

        title = 'Очистка сообщений'

        desc = f'''Канал: **#{ctx.channel.name}** 
Очищено сообщений: **{amount}**

Очистил: {ctx.author.mention}'''

        colour = discord.Colour.from_rgb(85, 255, 0)

        emb = discord.Embed(title=title, description=desc, colour=colour)
        emb.set_thumbnail(url=gifs['CLEAR'])

        await ctx.send(embed=emb)


def setup(client):
    client.add_cog(Clear(client))
