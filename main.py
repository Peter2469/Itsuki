import asyncio
import glob
import random
import sys
import traceback

import discord
from discord.ext import commands

import secret

G = ["i-", "I-"]

list_ext = glob.glob("cogs/*.py")  # Stores all .py files in a list to be used for startup

bot = commands.Bot(command_prefix=G)
bot.remove_command('help')
    
if __name__ == '__main__':
    count = 1

    for extension in list_ext:
        try:
            extensionz = extension.replace("\\", ".").replace("/", ".").replace(".py", "")
            bot.load_extension(extensionz)
            print(f"[Starting: {count}/{len(list_ext)}] Loaded up: {extension}")
            count = count + 1
        except Exception as e:
            print(f'[Failed] {extension} could not load!.', file=sys.stderr)
            traceback.print_exc()
            count = count + 1

@bot.event
async def on_ready():
    bot.fetch_offline_members = False
    print(f'[Loaded] Successfully logged in.')
    while True:
        activity = random.choice([f'{G[0]}help'])
        await asyncio.sleep(20)
        await bot.change_presence(activity=discord.Game(name=activity))

bot.run(secret.token, bot=True, reconnect=True)