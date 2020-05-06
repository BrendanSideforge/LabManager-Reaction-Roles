import discord 
from discord.ext import commands 
from datetime import datetime, timedelta 
import re 

inv = r'discord(\.com|\.gg)[\/invite\/]?(?:(?!.*[Ii10OolL]).[a-zA-Z0-9]{5,6}|[a-zA-Z0-9\-]{2,32})'

class AntiInvite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.Cog.listener()
    async def on_message(self, message):
        rere = re.compile(inv)
        invites = rere.findall(message.content)
        if invites:
            await message.delete(reason="Contained an invite.")
            await message.channel.send(f":ok_hand: No invites please.", delete_after=4)


def setup(bot):
    bot.add_cog(AntiInvite(bot))