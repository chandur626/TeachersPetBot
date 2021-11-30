"""
This file defines tests for links saving functions.
"""

import discord
from utils import wait_for_msg


async def test_links(testing_bot, commands_channel):
    async def wait(content):
        await wait_for_msg(testing_bot, commands_channel, content)

    await commands_channel.send('!send_links')
    await wait('The below list of messages contains URLs')


async def test(testing_bot, guild_id):
    commands_channel = discord.utils.get(testing_bot.get_all_channels(), name='q-and-a')
    guild = testing_bot.get_guild(guild_id)
    role = discord.utils.get(guild.roles, name="Instructor")
    member = guild.get_member(testing_bot.user.id)
    await member.add_roles(role)

    await test_links(testing_bot, commands_channel)
