import os

import discord
from discord.ext import commands


class Reload(commands.Cog, name=os.path.basename(__file__)[:-3]):
    def __init__(self, client):
        self.client = client


    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx):
        logs = []
        cogs_count = 0

        for file in os.listdir("cogs"):
            if file.endswith(".py"):
                cogs_count += 1
                try:
                    self.client.unload_extension(f"cogs.{file[:-3]}")
                    self.client.load_extension(f"cogs.{file[:-3]}")
                    logs.append("\n".join(["```css", f"name: {file[:-3]}", "status: reloaded", "```"])) 
                except Exception as e: 
                    logs.append("\n".join(["```fix", f"name: {file[:-3]}", "status: error", f"reason: {e}", "```"]))
        
        logs.append(f"```\nresult: {len(self.client.cogs)}/{cogs_count} cogs was reloaded```")

        await ctx.send(embed=discord.Embed(title="", description="\n".join(logs), colour=discord.Colour.from_rgb(47, 49, 54)))


    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, filename):
        try:
            self.client.load_extension(f"cogs.{filename}")
            result = "\n".join(["```css", f"name: {filename}", "status: loaded", "```"])
        except Exception as e: 
            result = "\n".join(["```fix", f"name: {filename}", "status: error", f"reason: {e}", "```"])
        
        await ctx.send(embed=discord.Embed(title="", description=result, colour=discord.Colour.from_rgb(47, 49, 54)))


    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, filename):
        try:
            self.client.unload_extension(f"cogs.{filename}")
            result = "\n".join(["```css", f"name: {filename}", "status: unloaded", "```"])
        except Exception as e: 
            result = "\n".join(["```fix", f"name: {filename}", "status: error", f"reason: {e}", "```"])
        
        await ctx.send(embed=discord.Embed(title="", description=result, colour=discord.Colour.from_rgb(47, 49, 54)))
        

    @commands.command()
    @commands.is_owner()
    async def reload_cog(self, ctx, filename):
        try:
            self.client.unload_extension(f"cogs.{filename}")
            self.client.load_extension(f"cogs.{filename}")
            result = "\n".join(["```css", f"name: {filename}", "status: reloaded", "```"])
        except Exception as e: 
            result = "\n".join(["```fix", f"name: {filename}", "status: error", f"reason: {e}", "```"])
        
        await ctx.send(embed=discord.Embed(title="", description=result, colour=discord.Colour.from_rgb(47, 49, 54)))
    

    @commands.command()
    @commands.is_owner()
    async def cogs(self, ctx):
        cogs = []
        for file in os.listdir("cogs"):
            if file.endswith(".py"):
                if file[:-3] in self.client.cogs.keys():
                    cogs.append(f"{file[:-3]} (loaded)")
                else:
                    cogs.append(f"{file[:-3]} (unloaded)")
        
        content = "```" + "\n".join(cogs) + "```"
        await ctx.send(embed=discord.Embed(title="", description=content, colour=discord.Colour.from_rgb(47, 49, 54)))
        

def setup(client):
    client.add_cog(Reload(client))
