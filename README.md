# Discord Bot Integration with OpenAI's GPT-3
This script demonstrates how to integrate Discord, a popular chat application, with OpenAI's GPT-3 AI model. The bot is designed to respond to user commands within Discord using the GPT-3 model for generating responses.

## Code Explanation
### Importing Libraries
StackEdit stores your files in your browser, which means all your files are automatically saved locally and are accessible **offline!**

### Create files and folders

    import os
    import discord
    from discord.ext import commands
    import openai
    from dotenv import load_dotenv

-   `os`: This module is used for interacting with the operating system, like reading environment variables.
-   `discord`: This is the main module for interacting with Discord.
-   `discord.ext.commands`: A framework for building commands for the Discord bot.
-   `openai`: The OpenAI module, used for communicating with OpenAI's API.
-   `dotenv`: A module for loading environment variables from a .env file.

-   `load_dotenv()`: This function loads environment variables from a `.env` file into the environment. This is typically used to keep sensitive information, like API keys, out of the source code.

        DISCORD_TOKEN = os.getenv('DISCORD_TOKEN') 
        OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
-   These lines retrieve the Discord bot token and OpenAI API key from the environment variables, which were set in the `.env` file.

`intents = discord.Intents.default()`
-   `discord.Intents`: This is used to specify which types of events the Discord bot should listen to. In this case, it's set to the default intents.
- ### Initializing OpenAI API

pythonCopy code

`openai.api_key = OPENAI_API_KEY` 

-   This line sets the API key for the OpenAI module, authorizing it to make requests to OpenAI's services.

### Initializing Discord Bot

`bot = commands.Bot(command_prefix='!', intents=intents)` 

-   This line creates a new instance of a Discord bot. The `command_prefix` is set to '!', meaning all commands for this bot will start with '!'.
-   `intents=intents`: The intents defined earlier are passed here.

### Event: on_ready

`@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')` 

-   `on_ready`: This asynchronous function is an event listener that gets called when the bot has successfully connected to Discord.
-   It prints a message to the console indicating the bot's name, confirming that it has logged in.

### Command: ask

`@bot.command()
async def ask(ctx, *, prompt):` 

-   `@bot.command()`: This decorator turns the following asynchronous function into a command that can be invoked within Discord.
-   `ctx`: This is the context through which the command was invoked.
-   `prompt`: The variable `prompt` captures all the text entered after the command name.

#### Command Functionality

 `try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=100  # Adjust as needed
        )
        await ctx.send(response.choices[0].text.strip())
    except Exception as e:
        await ctx.send(f"Error: {e}")` 

-   The command sends a request to OpenAI's GPT-3 API using the user's input as the prompt.
-   `openai.Completion.create`: This function sends a request to the OpenAI API with specified parameters.
-   `engine`: Specifies the GPT-3 model variant to use, in this case, 'davinci'.

-   `max_tokens`: This limits the length of the response.
-   The response from GPT-3 is sent back to the Discord channel. If there's an error, it sends an error message instead.

### Running the Bot

`bot.run(DISCORD_TOKEN)` 

-   Finally, this line starts the bot using the Discord token retrieved from the environment variables.
