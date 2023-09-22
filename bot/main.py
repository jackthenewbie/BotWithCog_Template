# main.py
from discord.ext import commands
from demo import demo
import discord
import json
with open("/home/coder/repo/botwithcogs/bot/token.json", "r") as f:
    secrets = json.load(f)


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix = ".", intents = intents)

    async def setup_hook(self) -> None:
        await self.tree.sync()
        await self.add_cog(demo.ExampleCog(self))
        print("Loaded extensions")
    async def on_command_error(self, ctx, error):
        await ctx.reply(error, ephemeral = True)
    
bot = Bot()


bot.run(secrets["DISCORD_TOKEN1"])