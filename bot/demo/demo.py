from discord.ext import commands
from discord import app_commands

class ExampleCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
	
    @commands.Cog.listener()
    async def on_ready(self) -> None:
        pass
	
    @commands.hybrid_command(name="commandx", with_app_command = True, description = "hybrid command")
    async def command(self, ctx: commands.Context) -> None:
        await ctx.reply("Hello world!", ephemeral=True)

    # doing something when the cog gets loaded
    async def cog_load(self):
        print(f"{self.__class__.__name__} loaded!")

    # doing something when the cog gets unloaded
    async def cog_unload(self):
        print(f"{self.__class__.__name__} unloaded!")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ExampleCog(bot))