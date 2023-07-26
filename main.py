import discord
from discord.ext import commands
import openai

# Set up intents
intents = discord.Intents.default()  # Default intents (typically enough for message sending/receiving)

# Initialize OpenAI API
openai.api_key = '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'

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

# Run the bot
bot.run('MTEzMzcxMjM2MzAxNTY0NzI2Nw.GR4hJ_.vAhsJUw1qmooZi1rF3gyXD42WWonhpI_A9_JkM')
