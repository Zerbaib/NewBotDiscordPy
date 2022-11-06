import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot
import json

with open("config.json") as file:
    config = json.load(file)

intents = discord.Intents.default()
bot = Bot(command_prefix=config["bot_prefix"], intents=intents)
bot.remove_command("help")

async def on_ready(self):
    print(f'Logged on as {self.user}!')

async def on_message(message):
    print(f'Message from {message.author}: {message.content}')

bot.run(config["token"])