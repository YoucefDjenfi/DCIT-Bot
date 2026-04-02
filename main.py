#!/usr/bin/env python3
"""
DCIT Bot – Algerian Cyber Law Assistant
Standalone version with only the /ask-law and /law-help commands.
"""

import discord
from discord.ext import commands
import logging
import os
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DCITBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        # Load the RAG cog
        await self.load_extension("bot.cogs.cyber_law_ai")
        # Sync slash commands globally
        await self.tree.sync()
        logger.info("✓ Synced slash commands")

    async def on_ready(self):
        logger.info(f"Bot ready! Logged in as {self.user}")


def main():
    bot = DCITBot()
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        logger.error("DISCORD_TOKEN not set in .env")
        return
    try:
        bot.run(token)
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Fatal error: {e}")


if __name__ == "__main__":
    main()