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
      if message.content.startswith("$ask"):
         ctx = message.content.split()
         ask_channel = client.get_channel(733594602287792149)
         question = ""
         for question_chunk in ctx[1:]:
            question += question_chunk
            if (ctx[1:].index(question_chunk) < len(ctx[1:]) - 1):
               question += " "
         await ask_channel.send(f"Người dùng tên **{message.author}** đã hỏi: *{question}*")



client.run(os.environ['DISCORD_TOKEN'])
