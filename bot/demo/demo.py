from discord.ext import commands
from discord import app_commands

class ExampleCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
	
    @commands.Cog.listener()
    async def on_ready(self) -> None:
        pass
	
    @commands.hybrid_command(name="command", with_app_command = True, description = "hybrid command")
    @app_commands.guilds()
    async def command(self, ctx: commands.Context) -> None:
        await ctx.reply("Hello world!", ephemeral=True)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ExampleCog(bot))