import os
import asyncio

import discord
from discord.ext import commands


class Bot:
    def __init__(self, token):
        self.client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
        self.token = token
        self.runned = False
        # self.client.remove_command('help')

        self.activity = discord.Game(name="")
        self.status = discord.Status.online

        for file in os.listdir("bot/cogs"):
            if file.endswith(".py"):
                try:
                    self.client.load_extension(f"bot.cogs.{file[:-3]}")
                except Exception as e:
                    print(e)

        self.statuses = {
            "В сети": discord.Status.online,
            "Не в сети": discord.Status.offline,
            "Не активный": discord.Status.idle,
            "Не беспокоить": discord.Status.dnd
        }

    def get_loaded_cogs(self):
        return self.client.cogs.keys()
    
    def get_guilds_count(self):
        return len(self.client.guilds)
    
    def get_members_count(self):
        members = 0

        for guild in self.client.guilds:
            members += len(guild.members)

        return members
    
    def load_cog(self, cog):
        self.client.load_extension(f"bot.cogs.{cog}")
    
    def unload_cog(self, cog):
        self.client.unload_extension(f"bot.cogs.{cog}")
    
    def activity_status_update(self, activity):
        self.status = self.statuses.get(activity, discord.Status.online)
        asyncio.run(self.client.change_presence(status=self.status, activity=self.activity))
        
    def status_update(self, status):
        self.activity = discord.Game(name=status)
        asyncio.run(self.client.change_presence(status=self.status, activity=self.activity))

    def run_bot(self):
        try:
            self.runned = True
            self.client.run(self.token)
        except:
            self.runned = False
