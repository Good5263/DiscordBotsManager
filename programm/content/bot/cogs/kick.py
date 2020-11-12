import discord
from discord.ext import commands

from content.bot.config import gifs


class Kick(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *reason):
        await ctx.message.delete()
        desc = f'''Был кикнут: {member.mention}
По причине: {" ".join(reason)}

Кикнул: {ctx.author.mention}'''

        colour = discord.Colour.from_rgb(85, 255, 0)

        emb = discord.Embed(title='Кик', description=desc, colour=colour)
        emb.set_thumbnail(url=gifs['KICK'])

        await ctx.send(embed=emb)
        await member.send(f'Вы были кикнуты с сервера {ctx.guild.name} по причине: {" ".join(reason)}')

        await member.kick(reason=' '.join(reason))


def setup(client):
    client.add_cog(Kick(client))
