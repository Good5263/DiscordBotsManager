import os

import discord
from discord.ext import commands


class Reload(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx):
        try:
            for file in os.listdir('./cogs'):
                if file.endswith('.py'):
                    self.client.unload_extension(f'cogs.{file[:-3]}')
                    self.client.load_extension(f'cogs.{file[:-3]}')
            print(f"Successfully updated {len(os.listdir('cogs'))} cogs!")

            await ctx.message.add_reaction('✅')
        except:
            await ctx.message.add_reaction('❎')

    @commands.command()
    @commands.is_owner()
    async def reload_cog(self, ctx, file):
        try:
            self.client.unload_extension(f'cogs.{file}')
            self.client.load_extension(f'cogs.{file}')
            print(f"{file} was updated")

            await ctx.message.add_reaction('✅')
        except:
            await ctx.message.add_reaction('❎')

    @commands.command()
    @commands.is_owner()
    async def cogs(self, ctx):
        try:
            desc = '\n'.join([file[:-3] for file in os.listdir('./cogs') if file.endswith('.py')])
            colour = discord.Colour.from_rgb(56, 24, 220)

            bot, owner = self.client.get_user(740101772441550888), self.client.get_user(662329339232256038)

            emb = discord.Embed(title='Cogs:', description=desc, colour=colour)
            emb.set_footer(text=f'{bot.name} by {owner}', icon_url=owner.avatar_url)

            await ctx.send(embed=emb)
        except:
            await ctx.message.add_reaction('❎')


def setup(client):
    client.add_cog(Reload(client))
