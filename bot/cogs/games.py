import os
import random

import discord
from discord.ext import commands


class Games(commands.Cog, name=os.path.basename(__file__)[:-3]):
    def __init__(self, client):
        self.client = client
    

    @commands.command()
    async def ball(self, ctx, *question):
        embed = discord.Embed(
            title="",
            description=f"**Вопрос:** `{' '.join(question)}`\n**Ответ:** ",
            colour=discord.Colour.from_rgb(190, 83, 212)
        )

        if question:
            answers = [
                "Да", "Нет", "Конечно", "Однозначно нет", "Я.. Не знаю(", ".. Бип-буп-бип",
                "Я думаю, что да", "Антон", "Да прибудет с тобой Google", "Нет, даже не думай о таком",
                "Я больше чем уверен, что да", "Да нет конечно", "Безусловно это так",
                "Error: very hard question for me", "А ты сам как считаешь?", "42",
                "Как много вопросов и так мало ответов", f"Спроси у {random.choice(ctx.guild.members)}. Ладно, шучу",
                "Естественно", "Нет, но это не точно", "Не знаю, отстань", "Да нет",
                "Спроси еще раз"
            ]
            embed.description += "`" + random.choice(answers) + "`"
        else:
            embed.description = f"**Вопрос:**\n**Ответ:** `Нет вопроса - нет ответа`"
        
        await ctx.send(embed=embed)
    

    @commands.command()
    async def money(self, ctx, side=None):
        embed = discord.Embed(title="", colour=discord.Colour.from_rgb(250, 242, 25))

        if side not in ["b", "h"]:
            embed.description = "Выберете одну из сторон b/h"
        else:
            if side == random.choice(["b", "h"]):
                embed.description = "Вы угадали!"
            else:
                embed.description = "Вы не угадали("
        
        await ctx.send(embed=embed)
    

def setup(client):
    client.add_cog(Games(client))
