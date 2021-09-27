from datetime import datetime, timedelta
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from discord_components import DiscordComponents, Button, ButtonStyle

import init_server
import event_creation
import cal
import office_hours
import profanity
import qna
import logging
import db

logging.basicConfig(level=logging.INFO)


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
#GUILD = 'TeachersPet-Dev'

intents=discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', description='This is TeachersPetBot!', intents=intents)


@bot.event
async def on_ready():
    DiscordComponents(bot)
    db.connect()
    event_creation.init(bot)
    office_hours.init(bot)
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):

    # allow messages from test bot
    if message.author.bot and message.author.id == 889697640411955251:
        ctx = await bot.get_context(message)
        await bot.invoke(ctx)

    if message.author == bot.user:
        return

    if(profanity.check_profanity(message.content)):
        await message.channel.send(message.author.name + ' says: ' + profanity.censor_profanity(message.content))
        await message.delete()

    await bot.process_commands(message)

    if message.content == 'hey bot':
        response = 'hey yourself'
        await message.channel.send(response)


@bot.event
async def on_message_edit(before, after):
    if profanity.check_profanity(after.content):
        await after.channel.send(after.author.name + ' says: ' + profanity.censor_profanity(after.content))
        await after.delete()


@bot.command()
async def test(ctx):
    await ctx.send('test successful')

@bot.command(name='create', help='Create a new event.')
# @commands.dm_only()
@commands.has_role('Instructor')
async def create_event(ctx):
    await event_creation.create_event(ctx)

# office hour commands
@bot.command(name='oh', help='Operations relevant for office hours.')
async def office_hour_command(ctx, command, *args):
    await office_hours.office_hour_command(ctx, command, *args)



@bot.command('ask')
async def ask_question(ctx, question):
    # make sure to check that this is actually being asked in the Q&A channel
    if ctx.channel.name == 'q-and-a':
        await qna.question(ctx, question)
    else:
        await ctx.author.send('Please send questions to the #q-and-a channel.')
        await ctx.message.delete()



@bot.command('answer')
async def answer_question(ctx, q_num, answer):
    # make sure to check that this is actually being asked in the Q&A channel
    if ctx.channel.name == 'q-and-a':
        await qna.answer(ctx, q_num, answer)
    else:
        await ctx.author.send('Please send answers to the #q-and-a channel.')
        await ctx.message.delete()


@bot.command('begin-tests')
async def begin_tests(ctx):
    if ctx.author.id != 889697640411955251:
        return
    
    test_oh_chan = next((ch for ch in ctx.guild.text_channels if 'office-hour-test' in ch.name), None)
    if test_oh_chan:
        quit(1)

    await office_hours.open_oh(ctx.guild, 'test')


@bot.command('end-tests')
async def end_tests(ctx):
    if ctx.author.id != 889697640411955251:
        return

    await office_hours.close_oh(ctx.guild, 'test')
    
    quit(0)


if __name__ == '__main__':
    bot.run(TOKEN)

def test_dummy():
    bot.run(TOKEN)