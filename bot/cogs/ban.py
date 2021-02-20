import discord
from discord.ext import commands

from bot.config import gifs


class Ban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *reason):
        await ctx.message.delete()
        desc = f'''Был забанен: {member.mention}
По причине: {" ".join(reason)}

Забанил: {ctx.author.mention}'''

        colour = discord.Colour.from_rgb(85, 255, 0)

        emb = discord.Embed(title='Бан', description=desc, colour=colour)
        emb.set_thumbnail(url=gifs['BAN'])

        await ctx.send(embed=emb)
        await member.send(f'Вы были забанены на сервере {ctx.guild.name} по причине: {" ".join(reason)}')

        await member.ban(reason=' '.join(reason))


def setup(client):
    client.add_cog(Ban(client))
