import discord
from discord.ext import commands

from random import choice, choices, randint


class Random(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def money(self, ctx):
        await ctx.message.delete()

        title, colour = choice(['Орёл', 'Решка']), discord.Colour.from_rgb(241, 249, 1)
        await ctx.send(embed=discord.Embed(title=title, colour=colour))

    @commands.command()
    async def password(self, ctx, amount: int = 8):
        await ctx.message.delete()

        ALL_SYMBOLS = 'QWERTYUIOPASDFGHJKLMNBVCXZqwertyuiopasdfghjklzxcvbnm1234567890-_'
        title, colour = choices(list(ALL_SYMBOLS), k=amount), discord.Colour.from_rgb(241, 249, 1)

        await ctx.author.send(embed=discord.Embed(title=''.join(title), colour=colour))

    @commands.command()
    async def random_int(self, ctx, start: int, end: int):
        await ctx.message.delete()

        await ctx.send(randint(start, end))

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def random_member(self, ctx):
        await ctx.message.delete()
        member, colour = choice(ctx.guild.members), discord.Colour.from_rgb(241, 249, 1)

        await ctx.send(embed=discord.Embed(title=f'{member.name}#{member.discriminator}', colour=colour))


def setup(client):
    client.add_cog(Random(client))
