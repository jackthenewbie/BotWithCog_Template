# main.py
from discord.ext import commands
import discord
import json
with open("token.json", "r") as f:
    secrets = json.load(f)


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix = ".", intents = intents)
    async def setup_hook(self) -> None:
        await self.load_extension("demo.demo")
        await self.tree.sync()
        print("Loaded extensions")
    async def on_command_error(self, ctx, error):
        await ctx.reply(error, ephemeral = True)
    
bot = Bot()


bot.run(secrets["DISCORD_TOKEN"])