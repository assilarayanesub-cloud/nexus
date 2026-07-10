import os
import discord
from discord.ext import commands

TOKEN = os.getenv("TOKEN")

WELCOME_CHANNEL_ID = 1519752500968820856  # ID du salon arrivées

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} est connecté !")
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)} commandes synchronisées.")
    except Exception as e:
        print(e)


@bot.tree.command(name="ping", description="Vérifie si le bot fonctionne")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🏓 Pong ! Le bot fonctionne.")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(WELCOME_CHANNEL_ID)

    if channel:
        embed = discord.Embed(
            title="🎉 Bienvenue sur Nexus !",
            description=f"Bienvenue {member.mention} !\nNous sommes heureux de t'accueillir sur le serveur.",
            color=discord.Color.blue()
        )

        embed.set_thumbnail(url=member.display_avatar.url)
        embed.set_footer(text=f"Membre n°{member.guild.member_count}")

        await channel.send(embed=embed)

        try:
            await member.send(
                f"👋 Salut {member.name} !\nBienvenue sur **Nexus**.\nNous espérons que tu passeras un bon moment !"
            )
        except:
            pass


bot.run(TOKEN)