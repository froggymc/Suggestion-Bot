import discord
from discord.ext import commands

bot_token = "put the discord bot token here!"

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f"{bot.user.display_name} is ready")


@bot.event
async def on_message(message):
    if message.channel.id == suggestion channel id:
        await message.add_reaction('👍')
        await message.add_reaction('👎')


bot.run(bot_token)
