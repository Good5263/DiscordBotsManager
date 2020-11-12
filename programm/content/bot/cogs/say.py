import discord
from discord.ext import commands

from content.bot.config import gifs


class Say(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def say(self, ctx, *args):
        await ctx.message.delete()
        await ctx.send(' '.join(args))

    @commands.command()
    @commands.is_owner()
    async def say_member(self, ctx, id_member: int, *args):
        await ctx.message.delete()
        member = self.client.get_user(id_member)
        await member.send(' '.join(args))

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def say_embed(self, ctx, *args):
        await ctx.message.delete()

        title, desc = ' '.join(args).split('|')
        colour = discord.Colour.from_rgb(56, 24, 220)

        await ctx.send(embed=discord.Embed(title=title, description=desc, colour=colour))

    @commands.command()
    @commands.is_owner()
    async def say_member_embed(self, ctx, id_member: int, *args):
        await ctx.message.delete()

        member = self.client.get_user(id_member)
        title, desc = ' '.join(args).split('|')
        colour = discord.Colour.from_rgb(56, 24, 220)

        await member.send(embed=discord.Embed(title=title, description=desc, colour=colour))


def setup(client):
    client.add_cog(Say(client))
