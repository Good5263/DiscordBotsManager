import os
import asyncio
from contextlib import redirect_stdout

import discord
from discord.ext import commands


class Bot:
    def __init__(self, token):
        self.client = commands.Bot(command_prefix='!')
        self.token = token
        # self.client.remove_command('help')

        self.activity = discord.Game(name="")
        self.status = discord.Status.online

        for file in os.listdir('bot/cogs'):
            if file.endswith('.py'):
                try:
                    self.client.load_extension(f'bot.cogs.{file[:-3]}')
                except Exception as e:
                    print(e)

        self.statuses = {
            'В сети': discord.Status.online,
            'Не в сети': discord.Status.offline,
            'Не активный': discord.Status.idle,
            'Не беспокоить': discord.Status.dnd
        }
    
    def load_cog(self, cog):
        self.client.load_extension(f'bot.cogs.{cog}')
    
    def unload_cog(self, cog):
        self.client.unload_extension(f'bot.cogs.{cog}')
    
    def activity_update(self, activity):
        self.activity = discord.Game(name=activity)
        asyncio.ensure_future(self.client.change_presence(status=self.status, activity=self.activity))

    def status_update(self, status):
        self.status = self.statuses[status]
        asyncio.ensure_future(self.client.change_presence(status=self.status, activity=self.activity))

    def on_bot(self):
        try:
            self.client.run(self.token)
        except:
            pass
