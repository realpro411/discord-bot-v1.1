import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='--', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir tenekeyim!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

@bot.command()
async def mem(ctx):
    resim = random.choice(os.listdir('memes'))
    with open(f'memes/{resim}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

bot.run("token girin")
