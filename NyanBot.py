import discord
from discord.ext import commands
import random
import requests
import urllib.request
from bs4 import BeautifulSoup

description = '''ghaskan's pet catbot.'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def cat():
    """Shows a random cat picture from random.cat."""
    r = requests.get('http://random.cat/meow')
    await bot.say(r.json()['file'])

@bot.command()
async def dog():
    """Shows a random cat picture from random.cat."""
    soup = BeautifulSoup(urllib.request.urlopen("http://random.dog/"), 'html.parser')
    for raw_img in soup.find_all('img'):
        link = raw_img.get('src')
        if link:
            await bot.say("http://random.dog/" + link)

@bot.command()
async def animals():
    """Shows a random cat picture from random.cat."""
    soup = BeautifulSoup(urllib.request.urlopen("http://www.animal-photos.org/shuffle/"))
    count = 0
    for raw_img in soup.find_all('img'):
        link = raw_img.get('src')
        if link:
            count += 1
            if count == 2:
                await bot.say(link)

@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)

@bot.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))

@bot.command()
async def repeat(times : int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await bot.say(content)

@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

@bot.group(pass_context=True)
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='bot')
async def _bot():
    """Is the bot cool?"""
    await bot.say('Yes, the bot is cool.')

bot.run('Mjg3NjE0ODM3Nzk2NjM0NjI0.C5x2_A.8P8HPpZ9WgozQGaMVGIe57jcmEk')
