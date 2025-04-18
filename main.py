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

@bot.command()
async def scemer(ctx):
    await ctx.send('<:scemer:1355236581992304700>')

oneriler = ["pet şişeleri saksı yapabilirsiniz",
         "plastik ve metal atıkları birleştirip süs eşyası olarak kullanabilirsiniz",
         "ilaç kutusunu kürdan ve pet şişe kapağı ile araba modeline çevirebilirsiniz",
         "gıda atıklarını toplatıp gübre olarak kullanabilirsiniz", "kırık cam parçalarından sanat icra edebilirsin"]

@bot.command()
async def oneri(ctx):
    await ctx.send(random.choice(oneriler))

bot.run("token girin")
