import discord
import asyncio
import os
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import Bot
from discord import Message
from discord import member
from discord import activity
from discord import guild



class Voice(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if after.channel != None:
            if after.channel.name == '음성채널 생성버튼':
                for guild in self.bot.guilds:
                    channel2 = await guild.create_voice_channel(name=f'{member.display_name} 의 채널', category=discord.utils.get(guild.categories, id=after.channel.category_id))
                    await member.move_to(channel2)
                    await channel2.set_permissions(member, connect=True, manage_channels=True)

                    def check(x, y, z):
                        return len(channel2.members) == 0
                    await self.bot.wait_for('voice_state_update', check=check)
                    await channel2.delete()



def setup(bot):
    bot.add_cog(Voice(bot))