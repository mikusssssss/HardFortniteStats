from redbot.core import commands
import discord
import aiohttp

SERVERS = {
    "Goob Station": [
        ("Goob Alpha", "https://alpha.goobstation.com/status"),
        ("Goob Sigma", "https://sigma.goobstation.com/status"),
        ("Goob Omega", "https://omega.goobstation.com/status"),
    ],
    "Monolith Station": [
        ("Monolith Inferno", "https://inferno.monolithstation.com/status"),
    ],
    "RMC": [
        ("Alamo", "https://alamo.rouny-ss14.com/status"),
    ],
}

class ServerStatus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="serverstatus")
    async def serverstatus(self, ctx):
        embed = discord.Embed(
            title="SS14 Server Status",
            color=discord.Color.blue()
        )

        async with aiohttp.ClientSession() as session:
            for host, servers in SERVERS.items():
                field_value = ""
                for name, url in servers:
                    try:
                        async with session.get(url, timeout=aiohttp.ClientTimeout(total=5)) as resp:
                            if resp.status == 200:
                                data = await resp.json(content_type=None)
                                players = data.get("players", "?")
                                soft_max = data.get("soft_max_players", "?")
                                map_name = data.get("map", "?")
                                real_name = data.get("name", name)
                                field_value += f"🟢 **{real_name}**\nPlayers: {players}/{soft_max} | Map: {map_name}\n\n"
                            else:
                                field_value += f"🔴 **{name}**\nServer unreachable\n\n"
                    except Exception:
                        field_value += f"🔴 **{name}**\nServer unreachable\n\n"

                embed.add_field(name=f"━━━ {host} ━━━", value=field_value.strip(), inline=False)

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(ServerStatus(bot))
