import json

import requests
from discord.ext import commands

with open('token.json') as f:
    TOKEN = json.load(f)['token']

bot = commands.Bot(command_prefix='!')


@bot.command(name='fun')
async def fun(context):
    response = requests.get('https://api.chucknorris.io/jokes/random').json()['value']\
        .replace('Chuck Norris', str(context.author.name))\
        .replace('CHUCK NORRIS', str(context.author.name))
    await context.send(response)

bot.run(TOKEN)
