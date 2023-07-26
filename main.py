import os
import discord
from discord.ext import commands
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve tokens from environment variables
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Set up intents for discord bot
intents = discord.Intents.default()

# Initialize OpenAI API
openai.api_key = OPENAI_API_KEY

# Initialize Discord bot with intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def ask(ctx, *, prompt):
    """Ask GPT-3 a question."""
    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=100  # Adjust as needed
        )
        await ctx.send(response.choices[0].text.strip())
    except Exception as e:
        await ctx.send(f"Error: {e}")

# Run the bot using the token from environment variable
bot.run(DISCORD_TOKEN)
