import discord
import response

token = "I'm too lazy to do this the correct way for a personal project :^)"

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        await response.parse_message(message)

def init_herbert():
    intents = discord.Intents.default()
    intents.message_content = True

    client = MyClient(intents=intents)
    client.run(token)
