import discord
from discord.ext import commands
from discord import app_commands
import logging
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from rag_query import answer_question

logger = logging.getLogger(__name__)

class CyberLawAI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ask-law", description="Posez une question sur le droit algérien du numérique")
    async def ask_law(self, interaction: discord.Interaction, question: str):
        await interaction.response.defer()
        try:
            answer = answer_question(question)
            # Discord has 2000 char limit
            if len(answer) > 1900:
                answer = answer[:1900] + "..."
            await interaction.followup.send(answer)
        except Exception as e:
            logger.error(f"Error in ask-law: {e}")
            await interaction.followup.send("Une erreur est survenue. Réessaie plus tard.")

    @app_commands.command(name="law-help", description="Affiche les informations sur le bot")
    async def law_help(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="⚖️ DCIT Cyber‑Law Assistant",
            description="Ce bot répond aux questions sur le droit algérien du numérique.",
            color=discord.Color.blue()
        )
        embed.add_field(name="📚 Sources", value="Code pénal (art. 394 bis–394 nonies), Loi 09‑04, Loi 18‑07, etc.", inline=False)
        embed.add_field(name="💡 Exemples", value="`/ask-law Puis-je scanner un réseau Wi‑Fi avec Nmap ?`\n`/ask-law Quelles sont les sanctions pour accès frauduleux ?`", inline=False)
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(CyberLawAI(bot))