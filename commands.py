import re
import discord
import random

async def send_message(channel: discord.channel, message):
    await channel.send(content=message, mention_author=True)

async def parse_command(message):
    command = message.content
    regex = re.compile('^!herbie ', re.I | re.S | re.IGNORECASE)
    command = re.sub(regex, '', command)

    # only one param
    command = command.split(' ')[0]

    if command.lower() == 'speak':
        await send_message(message.channel, "bark bark!!")
        return

async def duck(message):
    roll = random.randrange(73)
    if roll == 0:
        await send_message(message.channel, "https://headpat.xyz/uwu/duck/ely.png")
        return

    roll = random.randrange(73)
    if roll == 0:
        await send_message(message.channel, "https://headpat.xyz/uwu/duck/dwh.png")
        return

    images = [
        'angler.png',  'cat.png',       'dscim.png', 'eyepatch.png',  'HIYbQ63.png',   'plain.jpg',   'santa.png',     'tophat.png',
        'angry.png',   'cavalier.png',  'french.png',    'phat.png',      'rabbit.png',  'sashdumb.png',
        'anime.png',   'crown.png',     'hands.png',     'pinkhair.png',  'rage.jpg',    'snelm-1.png'
    ]

    number = random.randrange(len(images))
    await send_message(message.channel, "https://headpat.xyz/uwu/duck/" + images[number])

