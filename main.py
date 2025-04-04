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
async def troll(ctx, count_troll = 5):
    await ctx.send(("⠀⠀⠀⠀⠀⠀⢀⣴⠶⠶⠶⠶⠶⢶⢶⡶⡶⢶⣶⣶⡶⡶⡶⣶⣶⣶⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⣴⠏⠁⠀⣀⡰⣒⡭⣽⣒⣒⣒⣒⡒⠲⠲⠮⠯⠭⠷⠽⠽⠽⠭⠛⠷⣦⣀⠀⠀⠀\n⠀⠀⠀⠀⣼⠏⠀⠰⠚⡱⡪⠗⠉⠉⠀⠀⠀⠈⢇⠀⠀⠀⠀⢪⠋⠉⠉⠙⠲⡄⠀⠈⢹⡇⠀⠀\n⠀⠀⣠⣾⢇⠀⠀⠀⡈⡈⣡⣶⣾⣿⣿⡟⠷⣶⣄⠀⠀⠀⠀⠂⣠⣤⣴⣤⣄⢁⠀⠀⠘⣷⣄⠀\n⢠⣾⡟⢙⣹⣽⢵⣬⣝⢂⠛⠛⢙⣽⠏⠛⠷⣮⠿⠃⠀⠐⢶⣿⠿⠛⠛⠛⠙⠉⡙⡙⡽⡪⣟⣧\n⡟⢱⢡⣾⠃⢀⣶⣌⡙⠙⠛⠛⠛⠁⠀⠀⡀⢀⢀⠀⠀⠀⠈⣿⣄⠀⠀⢶⡴⡾⢛⠙⠻⢸⢸⣿\n⣷⣸⡘⣧⡚⠻⣯⡙⠛⢷⣦⣦⣄⡒⡒⠋⢽⡟⣭⣤⣄⠀⠀⠀⣹⣿⡦⣄⠀⢀⣾⣇⢀⣪⣼⡿\n⠘⢧⣕⡮⠅⠀⠹⣿⣷⣤⣿⣌⠉⠛⠻⢶⣮⣷⣬⣀⣀⣐⠳⢞⠋⣀⣀⣤⣵⣿⢿⣿⠈⢠⡿⠁\n⠀⠈⠻⣧⡀⠀⠀⠘⢷⡌⣿⠿⢿⣷⣦⣾⣇⣀⠈⠙⣿⠛⠛⣻⡟⠛⢙⣿⣀⣿⣼⣿⠇⢸⡇⠀\n⠀⠀⠀⠙⣧⡄⠀⠀⠀⠙⢿⣄⡀⠀⢹⡟⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢺⡇⠀\n⠀⠀⠀⠀⠘⢻⣦⡀⣄⡠⣀⡙⠻⢶⣾⣃⡀⠀⠀⢸⡇⠉⢉⣿⠋⢹⡟⢹⣟⣹⣿⠏⠀⢸⡇⠀\n⠀⠀⠀⠀⠀⠀⠈⠻⢶⣭⣚⠮⣑⡦⢅⣍⠛⠛⠟⠟⠗⠷⠿⠿⠞⠟⠟⠟⠛⢋⡄⠀⠀⢸⡇⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⢶⣭⣕⡳⠫⠾⢶⣶⣲⡨⠬⠬⠬⠤⠤⠴⠒⠋⣀⡔⠇⢸⡇⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢶⣦⣄⣄⣁⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⢀⣼⠇⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠻⠳⠶⠶⣦⣤⣤⣤⣤⠶⠶⠛⠁⠀⠀") * count_troll)

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

bot.run("token girin")
