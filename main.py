import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot
import json
import os
import sys

if not os.path.isfile("config.json"):
    sys.exit("ERROR: Le fichier 'config.json' n'a pas ete trouve !")
else:
    with open("config.json") as file:
        config = json.load(file)

intents = discord.Intents.default()
bot = Bot(command_prefix=config["prefix"], intents=intents)
bot.remove_command("help")

async def on_ready(self):
    print(f"Logged on as {self.user}!")

if __name__ == "__main__":
    for file in os.listdir("./cmd"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                bot.load_extension(f"cmd.{extension}")
                print(f"Extension chargee '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Echec du chargement de l'extension {extension}\n{exception}")

async def on_message(message):
    print(f'Message from {message.author}: {message.content}')

bot.run(config["token"])