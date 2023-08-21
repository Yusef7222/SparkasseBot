import discord

class Sparkasse:
    intents = None

    class MyClient(discord.Client):
        async def on_ready(self):
            print(f'Logged on as {self.user}!')

        async def on_message(self, message):
            print(f'Message from {message.author}: {message.content}')
    
    def setup_intents(message_content_intent: bool) -> None:
        Sparkasse.intents = discord.Intents.default()
        Sparkasse.intents.message_content = message_content_intent

    def execute_client(token: str) -> None:
        client = Sparkasse.MyClient(intents=Sparkasse.intents)
        client.run(token)