import discord
from discord.ext import commands
import os, random
import requests

# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event


async def on_ready():
    print(f'Fizemos login como {bot.user}')

@bot.command()
async def info(ctx):
    mensagem = """Você gostaria de aprender sobre qual item abaixo?
🧴 plastico 🧴
🍾 vidro 🍾
📄 papel 📄
🥫 metal 🥫
🌱 orgânico 🌱"""
    await ctx.send(mensagem)
                   
@bot.command()
async def plastico(ctx):
    await ctx.send(f'O plástico é um material que demora de 200 a 300 anos para se decompor. Para o bem dos animais, você deve descartar ele adequadamente, ou seja, no lixeiro vermelho')
        
@bot.command()
async def vidro(ctx):
    await ctx.send(f'O vidro demora milhares de anos para se decompor, mas pode ser reciclado infinitas vezes, o que torna seu descarte correto muito importante. Sempre tome cuidade para não se machucar e descarte ele no lixeiro verde')

@bot.command()
async def papel(ctx):
    await ctx.send(f'O papel se decompõe em poucos meses, mas seu consumo excessivo ainda causa impactos ambientais, por isso a reciclagem é essencial. Poupe as arvores e descarte ele no lixeiro azul')

@bot.command()
async def metal(ctx):
    await ctx.send(f'O metal demora muitos anos para se decompor, mas pode ser reciclado várias vezes, sendo muito importante para a preservação dos recursos naturais. Seja inteligente e descarte ele no lixeiro amarelo')

@bot.command()
async def organico(ctx):
    await ctx.send(f'O lixo orgânico se decompõe rapidamente e pode virar adubo, sendo uma ótima forma de reduzir o desperdício. Ajude a natureza a se renovar: use o lixeiro marrom.')
