import discord
import os
my_secret = os.environ['TOKEN']

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

        if (message.content.startswith("Hello") or message.content.startswith('hello') or message.content.startswith('hey') or
        message.content.startswith('Hey')
        or message.content.startswith('Hi')
        or message.content.startswith('hi')):

          text = message.content.split(" ")[0]
          await message.channel.send(text + " @" +str(message.author))

client = MyClient()
client.run(my_secret)