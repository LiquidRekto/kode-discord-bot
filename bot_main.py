import os
import discord

client = discord.Client()

@client.event
async def on_message(message):
   if message.author.bot:
      return
   else:
      if message.content.startswith("WASSUP"):
         await message.channel.send(f"WASSUP {message.author.mention}")



client.run(os.environ['DISCORD_TOKEN'])