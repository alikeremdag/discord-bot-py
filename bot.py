import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def sa(ctx):
    await ctx.send("as" * count_heh)

@bot.command()
async def nasılsın(ctx):
    await ctx.send("iyiyim sen" * count_heh)
@bot.command()
async def iyiyim(ctx):
    await ctx.send("ok" * count_heh)


bot.run("botunuzun ipini girin")
