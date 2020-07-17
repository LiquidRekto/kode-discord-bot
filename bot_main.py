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
         moderator = discord.utils.get(message.guild.roles, id=733580724912783420)
         await ask_channel.send(f"{moderator.mention}\nNgười dùng tên **{message.author}** đã hỏi: \n*{question}*")
      if message.content.startswith("$rmvmsg"):
         ctx = message.content.split()
         if ctx[1].isnumeric():
            msg_num = int(ctx[1])
            msg = []
            lists = await message.channel.history(limit=msg_num+1).flatten()
            for x in lists:
               msg.append(x)
            await message.channel.delete_messages(msg)
            await message.channel.send(f"{message.author.mention} Bạn đã xoá %s tin nhắn!" % ctx[1])
         else:
            await message.channel.send(f"{message.author.mention}\nKhông thể thực hiện lệnh!\nLí do: *Lỗi nhập liệu*")



client.run(os.environ['DISCORD_TOKEN'])
