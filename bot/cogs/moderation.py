import os
import asyncio

import discord
from discord.ext import commands


class Moderation(commands.Cog, name=os.path.basename(__file__)[:-3]):
    def __init__(self, client):
        self.client = client
    

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *reason):
        await ctx.message.delete()

        embed = discord.Embed(
            title="",
            description=f"{ctx.author.mention} забанил {member.mention}",
            colour=discord.Colour.from_rgb(63, 242, 239)
        )

        await member.send(f"Вы были забанены на сервере {ctx.guild.name} по причине: {' '.join(reason)}.")
        await ctx.send(embed=embed)
        await member.ban(reason=" ".join(reason))
    

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *reason):
        await ctx.message.delete()

        embed = discord.Embed(
            title="",
            description=f"{ctx.author.mention} выгнал {member.mention}",
            colour=discord.Colour.from_rgb(63, 242, 239)
        )

        await member.send(f"Вы были кикнуты с сервера {ctx.guild.name} по причине: {' '.join(reason)}.")
        await ctx.send(embed=embed)
        await member.kick(reason=" ".join(reason))
    

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def temp_role(self, ctx, role: discord.Role, member: discord.Member, time=None):
        await ctx.message.delete()
        embed = discord.Embed(
            title="",
            description=f"{ctx.author.mention} выдал роль {role.mention} пользователю {member.mention}",
            colour=discord.Colour.from_rgb(63, 242, 239)
        )
        await ctx.send(embed=embed)
        await member.add_roles(role)
        if time is not None:
            await asyncio.sleep(int(time))
            await member.remove_roles(role)
    

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.message.delete()

        if 0 < amount <= 200:
            await ctx.channel.purge(limit=amount)
            answer = await ctx.send(f"{ctx.author} очистил {amount} сообщений")
        else:
            answer = await ctx.send(f"Количество сообщений должно быть больше 0 и не превосходить 200")
        
        await asyncio.sleep(5)
        await answer.delete()


def setup(client):
    client.add_cog(Moderation(client))
