import discord 
from discord.ext import commands 

class Reaction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        # get the message id from payload
        message = payload.message_id 

        # this will see if the payload message id is the same as another message id
        if message == 707083141231411250:
            
            # get the guild id from payload
            guild_id = payload.guild_id
            guild = self.bot.get_guild(guild_id)

            # see if the payload emoji name is the same as another one 
            if payload.emoji.name == "🔔":
                # get the role
                role = discord.utils.get(guild.roles, name="Dev")

                # get the user
                user = guild.get_member(payload.user_id)

                # add the role to the user
                await user.add_roles(role, reason="Reaction roles for the 🔔 emoji.")

                # send a mesage to the user saying that they have successfully gottn the role
                try:
                    print("Trying to dm the user")
                    await user.send(f":tada: You have gotten the **{role.name}** role for clicking the 🔔 reaction!")
                except:
                    print("Couldn't dm the user, so I am going to try and send the message in the channel.")
                    # get the channel so that it can notify them there
                    channel = guild.get_channel(695887553890484225)

                    # send the congrats message there 
                    # delete after 4 seconds so that it doesn't flood the chat
                    await channel.send(f":tada: {user.mention}, you have gotten the **{role.name}** role for clicking the 🔔 reaction!", delete_after=4)
            elif payload.emoji.name == "🌐":
                # get the role
                role = discord.utils.get(guild.roles, name="Muted")

                # get the user
                user = guild.get_member(payload.user_id)

                # add the role to the user
                await user.add_roles(role, reason="Reaction roles for the 🌐 emoji.")

                # send a mesage to the user saying that they have successfully gottn the role
                try:
                    print("Trying to dm the user")
                    await user.send(f":tada: You have gotten the **{role.name}** role for clicking the 🌐 reaction!")
                except:
                    print("Couldn't dm the user, so I am going to try and send the message in the channel.")
                    # get the channel so that it can notify them there
                    channel = guild.get_channel(695887553890484225)

                    # send the congrats message there 
                    # delete after 4 seconds so that it doesn't flood the chat
                    await channel.send(f":tada: {user.mention}, you have gotten the **{role.name}** role for clicking the 🌐 reaction!", delete_after=4)
            elif payload.emoji.name == "🚓":
                # get the role
                role = discord.utils.get(guild.roles, name="911")

                # get the user
                user = guild.get_member(payload.user_id)

                # add the role to the user
                await user.add_roles(role, reason="Reaction roles for the 🚓 emoji.")

                # send a mesage to the user saying that they have successfully gottn the role
                try:
                    print("Trying to dm the user")
                    await user.send(f":tada: You have gotten the **{role.name}** role for clicking the 🚓 reaction!")
                except:
                    print("Couldn't dm the user, so I am going to try and send the message in the channel.")
                    # get the channel so that it can notify them there
                    channel = guild.get_channel(695887553890484225)

                    # send the congrats message there 
                    # delete after 4 seconds so that it doesn't flood the chat
                    await channel.send(f":tada: {user.mention}, you have gotten the **{role.name}** role for clicking the 🚓 reaction!", delete_after=4)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        # get the message id from payload
        message = payload.message_id 

        # this will see if the payload message id is the same as another message id
        if message == 707083141231411250:
            
            # get the guild id from payload
            guild_id = payload.guild_id
            guild = self.bot.get_guild(guild_id)

            # see if the payload emoji name is the same as another one 
            if payload.emoji.name == "🔔":
                # get the role
                role = discord.utils.get(guild.roles, name="Dev")

                # get the user
                user = guild.get_member(payload.user_id)

                # add the role to the user
                await user.remove_roles(role, reason="Reaction roles for the 🔔 emoji.")

                # send a mesage to the user saying that they have successfully gottn the role
                try:
                    print("Trying to dm the user")
                    await user.send(f":tada: You have removed the **{role.name}** role for clicking the 🔔 reaction!")
                except:
                    print("Couldn't dm the user, so I am going to try and send the message in the channel.")
                    # get the channel so that it can notify them there
                    channel = guild.get_channel(695887553890484225)

                    # send the congrats message there 
                    # delete after 4 seconds so that it doesn't flood the chat
                    await channel.send(f":tada: {user.mention}, you have removed the **{role.name}** role for clicking the 🔔 reaction!", delete_after=4)
            elif payload.emoji.name == "🌐":
                # get the role
                role = discord.utils.get(guild.roles, name="Muted")

                # get the user
                user = guild.get_member(payload.user_id)

                # remove the role to the user
                await user.remove_roles(role, reason="Reaction roles for the 🌐 emoji.")

                # send a mesage to the user saying that they have successfully removed the role from themselves
                try:
                    print("Trying to dm the user")
                    await user.send(f":tada: You have removed the **{role.name}** role for clicking the 🌐 reaction!")
                except:
                    print("Couldn't dm the user, so I am going to try and send the message in the channel.")
                    # get the channel so that it can notify them there
                    channel = guild.get_channel(695887553890484225)

                    # send the congrats message there 
                    # delete after 4 seconds so that it doesn't flood the chat
                    await channel.send(f":tada: {user.mention}, you have removed the **{role.name}** role for clicking the 🌐 reaction!", delete_after=4)
            elif payload.emoji.name == "🚓":
                # get the role
                role = discord.utils.get(guild.roles, name="911")

                # get the user
                user = guild.get_member(payload.user_id)

                # re,pve the role to the user
                await user.remove_roles(role, reason="Reaction roles for the 🚓 emoji.")

                # send a mesage to the user saying that they have successfully removed the role from themselves
                try:
                    print("Trying to dm the user")
                    await user.send(f":tada: You have removed the **{role.name}** role for clicking the 🚓 reaction!")
                except:
                    print("Couldn't dm the user, so I am going to try and send the message in the channel.")
                    # get the channel so that it can notify them there
                    channel = guild.get_channel(695887553890484225)

                    # send the congrats message there 
                    # delete after 4 seconds so that it doesn't flood the chat
                    await channel.send(f":tada: {user.mention}, you have removed the **{role.name}** role for clicking the 🚓 reaction!", delete_after=4)

def setup(bot):
    bot.add_cog(Reaction(bot))