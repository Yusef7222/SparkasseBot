import discord
from loguru import logger


class Sparkasse:
    intents = None

    class MyClient(discord.Client):
        async def on_ready(self):
            logger.debug(f"Successfully logged in as {self.user}")

        async def on_message(self, message):
            if message.author == self.user:
                return
            
            if message.content.startswith('$send'):
                await message.channel.send('Sending money!')
    
    def setup_intents(message_content_intent: bool) -> None:
        Sparkasse.intents = discord.Intents.default()
        Sparkasse.intents.message_content = message_content_intent

    def execute_client(token: str) -> None:
        if Sparkasse.intents == None or Sparkasse.intents == False:
            logger.debug("Intents have been disabled!")
            
        client = Sparkasse.MyClient(intents=Sparkasse.intents)
        client.run(token)