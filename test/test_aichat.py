import unittest
import discord

class TestAichat(unittest.TestCase):
    def setUp(self):
        # Create a Discord bot instance with a command prefix
        self.bot = discord.ext.commands.Bot(command_prefix='!')
        self.ctx = discord.ext.commands.Context(prefix='!', bot=self.bot)

    def test_aichat_exit(self):
        # Simulate a user entering "exit" in the chat
        user_input = discord.Message(content="exit", author=discord.User(), channel=discord.TextChannel())

        # Simulate the user context for the bot
        self.ctx.author = user_input.author
        self.ctx.channel = user_input.channel

        # Get the Aichat command and run it
        aichat_command = self.bot.get_command('Aichat')
        with self.assertLogs(self.bot, level='INFO') as logs:
            self.bot.dispatch('message', user_input)
        
        # Check for expected log messages
        log_messages = [record.getMessage() for record in logs.records]
        self.assertIn("You are now in an AI chat session. Type 'exit' to end the chat.", log_messages)
        self.assertIn("Chat session ended.", log_messages)

    def test_aichat_timeout(self):
        # Simulate a timeout in the chat session
        self.ctx.author = discord.User()
        self.ctx.channel = discord.TextChannel()

        # Get the Aichat command and run it
        aichat_command = self.bot.get_command('Aichat')
        with self.assertLogs(self.bot, level='INFO') as logs:
            self.bot.dispatch('message', discord.Message())
        
        # Check for expected log messages
        log_messages = [record.getMessage() for record in logs.records]
        self.assertIn("You are now in an AI chat session. Type 'exit' to end the chat.", log_messages)
        self.assertIn("Chat session timed out. Type `!chat` to start a new session.", log_messages)
