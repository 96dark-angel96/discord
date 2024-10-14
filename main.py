from config import TOKEN
import discord
from discord import Message

bot = discord.Bot(intents=discord.Intents.all())


@bot.event
async def on_message(m:Message):
    if m.author.bot:
        return
    if m.content=="досвидания":
        await m.channel.send("иди от сюда")
    elif m.content=="бан":
        await m.channel.send("за что")
    elif m.content=="за читы":
        await m.channel.send("а")
    else:
        await m.reply(m.content)


bot.run(TOKEN)
