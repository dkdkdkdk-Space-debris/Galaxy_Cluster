import discord
from discord.ext import commands

fleeticon = 'https://cdn.discordapp.com/attachments/695628083801358396/708318261611200623/300x300orang.png'#아이콘 이미지
bot=commands
class Function(commands.Cog):

    def __init__(self,bot):
        self.bot=bot

def setup(bot):
    bot.add_cog(Function(bot))