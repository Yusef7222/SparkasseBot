import discord
from loguru import logger
import random
import json

class Sparkasse:
    intents = None

    class MyClient(discord.Client):
        async def on_ready(self):
            logger.debug(f"Successfully logged in as {self.user}")

        async def on_message(self, message):
            if message.author == self.user:
                return

            if message.content.startswith('$register'):
                with open('users.json', 'r') as users_data:
                    data = json.load(users_data)

                    if str(message.author.id) in data:
                        await message.channel.send('User is already registered in database!')
                    else:
                        await message.channel.send('Registering user...')
                        data[str(message.author.id)] = random.randint(100000, 999999)

                        with open('users.json', 'w') as users_data:
                            json.dump(data, users_data)
                            
                        await message.channel.send('User registered!')

            
    def setup_intents(message_content_intent: bool) -> None:
        Sparkasse.intents = discord.Intents.default()
        Sparkasse.intents.message_content = message_content_intent

    def execute_client(token: str) -> None:
        if Sparkasse.intents == None or Sparkasse.intents == False:
            logger.debug("Intents have been disabled!")
            
        client = Sparkasse.MyClient(intents=Sparkasse.intents)
        client.run(token)