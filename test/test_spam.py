###########################
# Tests Spam
###########################
from time import sleep
import discord
from utils import wait_for_msg

###########################
# Function: test
# Description: runs each test
# Inputs:
#      - testing_bot: bot that sends commands to test TeachersPetBot
#      - guild_id: id of the guild that is using the TeachersPetBot
# Outputs: None
###########################
async def test(testing_bot, guild_id):
    commands_channel = next(
        ch for ch in testing_bot.get_guild(guild_id).text_channels if ch.name == 'instructor-commands')
    # Add instructor role to bot
    guild = testing_bot.get_guild(guild_id)
    role = discord.utils.get(guild.roles, name="Instructor")
    member = guild.get_member(testing_bot.user.id)
    await member.add_roles(role) # so we can test the !set_spam_settings command

    await start_invalid_settings(testing_bot, commands_channel)
    await test_valid_settings(testing_bot, commands_channel)
    #await test_invalid_timeout_time(testing_bot, commands_channel)
    #await test_spam(testing_bot)

async def start_invalid_settings(testing_bot, commands_channel):
    await test_invalid_warning_num(testing_bot, commands_channel)
    #await test_invalid_timeout_num(testing_bot, commands_channel)
    #await test_invalid_clear_time(testing_bot, commands_channel)
    #await test_invalid_timeout_time(testing_bot, commands_channel)


async def test_invalid_warning_num(testing_bot, commands_channel):
    await commands_channel.send('!set_spam_settings')
    await wait_for_msg(testing_bot, commands_channel, 'How many messages should a user '
                                                      'be able to send before they are warned of spamming?')
    # above wait for the expected response, else it throws an exception in the function wait_for_msg

    await commands_channel.send('90hoq03')
    await wait_for_msg(testing_bot, commands_channel, 'Invalid entry. Try again...')

    await test_invalid_timeout_num(testing_bot, commands_channel)



async def test_invalid_timeout_num(testing_bot, commands_channel):
    await commands_channel.send('!set_spam_settings')
    await wait_for_msg(testing_bot, commands_channel, 'How many messages should a user '
                                                      'be able to send before they are warned of spamming?')
    # above wait for the expected response, else it throws an exception in the function wait_for_msg

    await commands_channel.send('4')
    await wait_for_msg(testing_bot, commands_channel, 'How many messages should a user '
                                                      'be able to send before they are put in timeout?')
    await commands_channel.send('+')
    await wait_for_msg(testing_bot, commands_channel, 'Invalid entry. Try again...')

    await test_invalid_clear_time(testing_bot, commands_channel)


async def test_invalid_clear_time(testing_bot, commands_channel):
    await commands_channel.send('!set_spam_settings')
    await wait_for_msg(testing_bot, commands_channel, 'How many messages should a user '
                                                      'be able to send before they are warned of spamming?')
    # above wait for the expected response, else it throws an exception in the function wait_for_msg

    await commands_channel.send('4')
    await wait_for_msg(testing_bot, commands_channel, 'How many messages should a user '
                                                      'be able to send before they are put in timeout?')
    await commands_channel.send('5')
    await wait_for_msg(testing_bot, commands_channel, 'How much time should users have to send 4 messages '
                                                      'before they will be warned and then eventually put in timeout?')
    await commands_channel.send('beezleopop')
    await wait_for_msg(testing_bot, commands_channel, 'Invalid entry. Try again...')

    await test_invalid_timeout_time(testing_bot, commands_channel)

async def test_invalid_timeout_time(testing_bot, commands_channel):
    await commands_channel.send('!set_spam_settings')
    await wait_for_msg(testing_bot, commands_channel, 'How many messages should a user '
                                                      'be able to send before they are warned of spamming?')
    # above wait for the expected response, else it throws an exception in the function wait_for_msg

    await commands_channel.send('4')
    await wait_for_msg(testing_bot, commands_channel, 'How many messages should a user '
                                                      'be able to send before they are put in timeout?')
    await commands_channel.send('5')
    await wait_for_msg(testing_bot, commands_channel, 'How much time should users have to send 4 messages '
                                                      'before they will be warned and then eventually put in timeout?')
    await commands_channel.send('15')
    await wait_for_msg(testing_bot, commands_channel,
                       'How long should a user be placed in timeout when caught spamming? '
                       'Format: min,hours,days Example: 5,0,0 is 5 minutes')
    await commands_channel.send('1')
    await wait_for_msg(testing_bot, commands_channel, 'Invalid entry. Try again...')


async def test_valid_settings(testing_bot, commands_channel):
    await commands_channel.send('!set_spam_settings')
    await wait_for_msg(testing_bot, commands_channel, 'How many messages should a user '
                                                      'be able to send before they are warned of spamming?')
    # above wait for the expected response, else it throws an exception in the function wait_for_msg

    await commands_channel.send('4')
    await wait_for_msg(testing_bot, commands_channel, 'How many messages should a user '
                                                      'be able to send before they are put in timeout?')
    await commands_channel.send('5')
    await wait_for_msg(testing_bot, commands_channel, 'How much time should users have to send 4 messages '
                                                      'before they will be warned and then eventually put in timeout?')
    await commands_channel.send('15')
    await wait_for_msg(testing_bot, commands_channel, 'How long should a user be placed in timeout when caught spamming? '
                           'Format: min,hours,days Example: 5,0,0 is 5 minutes')
    await commands_channel.send('5,0,0')
    await wait_for_msg(testing_bot, commands_channel, 'Spam settings successfully updated!')

"""
async def test_spam(testing_bot):
    qna_channel = discord.utils.get(testing_bot.get_all_channels(), name='q-and-a')
    await qna_channel.send('shit')
    await ctx.send("message 1")
    await ctx.send("message 2")
    await ctx.send("message 3")
    await ctx.send("message 4")
    await ctx.send("message 5")
    await ctx.send("message 6")
    #messages = await qna_channel.history(limit=1).flatten()
    messages = [message async for message in qna_channel.history(limit=1)]
"""





