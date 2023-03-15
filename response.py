import re
import discord
import twitter
import commands
import datetime

timeouts = {}

async def send_message(channel: discord.channel, message):
    await channel.send(content=message, mention_author=True)

def get_timeout(message):
    userid = message.author.id
    timestamp = int(datetime.datetime.timestamp(datetime.datetime.now()))
    if userid in timeouts.keys():
        if timestamp - timeouts[userid] > 30:
            timeouts[userid] = timestamp
            return True
        else:
            return False
    else:
        timeouts[userid] = timestamp
        return True


async def parse_message(message):
    post = message.content
    search = re.search('https://twitter.com', post, re.I | re.S | re.IGNORECASE)

    command = re.search('^!herbie ', post, re.I | re.S | re.IGNORECASE)
    duck = re.search('^r!duck', post, re.I | re.S | re.IGNORECASE)

    if command:
        await commands.parse_command(message)
        return

    if duck:
        if get_timeout(message):
            await commands.duck(message)
        else:
            await message.delete()
        return

    if search:
        # with a video returns attachments: {media_keys: [ "7_1616167227056881664" ] }
        # post_id = "1616168123241222146"
        # without a video simply returns nothing for media id
        # post_id = "1616227878730928130"
        # with an image returns media keys "3_1838192381231"
        # post_id = "1616435483760005135"
        ###############################3
        # video = 7
        # image = 3
        # gif = 16

        post_id = re.search(r"status/(\d*)", post)

        if post_id is None:
            return

        post_id = post_id.group(1)
        has_video = twitter.check_twitter(post_id)

        if has_video:
            await message.delete()
            post = post.replace('https://twitter.com', 'https://vxtwitter.com')
            channel = message.channel
            user = message.author.id
            response = (f'User <@{user}> sent the following message without a vxtwitter link! Sad!\n\n' + post)
            await send_message(channel, response)
