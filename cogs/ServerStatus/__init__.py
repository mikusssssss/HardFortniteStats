from .serverstatus import ServerStatus

async def setup(bot):
    await bot.add_cog(ServerStatus(bot))
