import discord 
from discord.ext import commands 

TOKEN = "NzA3MDc3ODg1NDQ1NDA2NzUw.XrDjnA.TVD-KH_XcQnSWNGtRwCeDoLHdx8"

cogs = ["cogs.reactions"]

class ReactionRoles(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="?", case_insensitive=True)

    async def on_ready(self):
        print("Bot is online")

bot = ReactionRoles()

if __name__ == '__main__':
    for cog in cogs:
        try:
            bot.load_extension(cog)
            print(f"Loaded {cog} successfully.")
        except Exception as e:
            print(f"Couldn't load {cog}: {e}")

bot.run(TOKEN)
