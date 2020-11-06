import os
import asyncio

import discord
from discord.ext import commands


class Bot:
    def __init__(self, token):
        self.client = commands.Bot(command_prefix='!')
        self.token = token
        # self.client.remove_command('help')

        self.activity = discord.Game(name="")
        self.status = discord.Status.online

        for file in os.listdir('./content/bot/cogs'):
            if file.endswith('.py'):
                #try:
                self.client.load_extension(f'content.bot.cogs.{file[:-3]}')
                #except:
                #    print('Error')

        self.statuses = {
            'В сети': discord.Status.online,
            'Не в сети': discord.Status.offline,
            'Не активный': discord.Status.idle,
            'Не беспокоить': discord.Status.dnd
        }
    
    def get_all_guilds(self):
        return self.client.guilds
    
    def get_members(self, guild):
        return guild.members 
    
    def get_roles(self, guild):
        return guild.roles
    
    def load_cog(self, cog):
        self.client.load_extension(f'content.bot.cogs.{cog}')
    
    def unload_cog(self, cog):
        self.client.unload_extension(f'content.bot.cogs.{cog}')
    
    def get_name(self):
        return str(self.client.user)
    
    def activity_update(self, activity):
        self.activity = discord.Game(name=activity)

        asyncio.ensure_future(self.client.change_presence(status=self.status, activity=self.activity))

    def status_update(self, status):
        self.status = self.statuses[status]

        asyncio.ensure_future(self.client.change_presence(status=self.status, activity=self.activity))

    def start_bot(self):
        self.client.run(self.token)
