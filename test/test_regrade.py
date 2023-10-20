"""
   Tests Regrade
"""

from time import sleep
import discord


async def test(testing_bot, guild_id):

    """
        Function: test
        Description: runs each test
        Inputs:
            - testing_bot: bot that sends commands to test TeachersPetBot
            - guild_id: id of the guild that is using the TeachersPetBot
        Outputs: None
    """
    await test_regrade_request(testing_bot)
    await test_update_request(testing_bot)
    await test_display_requests(testing_bot)
    await test_remove_request(testing_bot)


async def  test_regrade_request(testing_bot):

    """
        Function: test_regrade_request
        Description: tests regrade-request command
        Inputs:
           - testing_bot: bot that sends commands to test TeachersPetBot
        Outputs: None
    """

    print('testing regrade request')
    regrade_channel = discord.utils.get(testing_bot.get_all_channels(), name='regrade-requests')
    await regrade_channel.send('!regrade-request "Student 1" q1,q2,q3')
    sleep(5.0)
    #messages = await regrade_channel.history(limit=1).flatten()
    messages = [message async for message in regrade_channel.history(limit=1)]

    for m in messages:
        new_request = "STUDENT 1's regrade request successfully submitted" in m.content
        duplicate_request = "Duplicate regrade request.Use !regrade-update command to make updates to request"
        assert (new_request or duplicate_request)


async def test_update_request(testing_bot):

    """
        Function: test_update_request
        Description: tests update-request command
        Inputs:
           - testing_bot: bot that sends commands to test TeachersPetBot
        Outputs: None
    """
    print('testing update request')
    regrade_channel = discord.utils.get(testing_bot.get_all_channels(), name='regrade-requests')
    await regrade_channel.send('!update-request "Student 1" q4,q5,q6')
    sleep(5.0)
    #messages = await regrade_channel.history(limit=1).flatten()
    messages = [message async for message in regrade_channel.history(limit=1)]
    for m in messages:
        assert "STUDENT 1's regrade request updated successfully" in m.content


async def test_display_requests(testing_bot):

    """
        Function: test_display_requests
        Description: tests display-requests command
        Inputs:
           - testing_bot: bot that sends commands to test TeachersPetBot
        Outputs: None
    """
    print('testing display requests')
    regrade_channel = discord.utils.get(testing_bot.get_all_channels(), name='regrade-requests')
    await regrade_channel.send('!display-requests')
    sleep(5.0)
    #messages = await regrade_channel.history(limit=1).flatten()
    messages = [message async for message in regrade_channel.history(limit=1)]
    for m in messages:
        assert 'STUDENT 1 q4,q5,q6' in m.content


async def test_remove_request(testing_bot):

    """
        Function: test_remove_request
        Description: tests remove-request command
        Inputs:
           - testing_bot: bot that sends commands to test TeachersPetBot
        Outputs: None
    """
    print('testing remove request')
    regrade_channel = discord.utils.get(testing_bot.get_all_channels(), name='regrade-requests')
    await regrade_channel.send('!remove-request "Student 1" q4,q5,q6')
    sleep(5.0)
    #messages = await regrade_channel.history(limit=1).flatten()
    messages = [message async for message in regrade_channel.history(limit=1)]
    for m in messages:
        assert "STUDENT 1's regrade request removed successfully" in m.content
