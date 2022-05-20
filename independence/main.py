'''
   Galaxy Cluster


    DK_Dynamics
    By dkdkdkdk
     이승준#8326


'''


import discord             #디스코드 모듈
import asyncio             #아나시코 모듈
import random              #랜덤 모듈
import pytz                #
import urllib.request      #크롤링
import requests            #크롤링
import math
import gspread
import os
import youtube_dl
import sys
import pandas as pd
from time import *
from datetime import *
from pytz import *
from bs4 import BeautifulSoup
from pytz import timezone
from datetime import timezone
from datetime import timedelta
from datetime import tzinfo
from oauth2client.service_account import ServiceAccountCredentials
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import Bot
from discord import Message
from discord import member
from discord import activity
from discord import guild
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import  create_choice, create_option
from FunctionFunction import *


bot = Bot(command_prefix='!', intents=discord.Intents.all(), strip_after_prefix=False, case_insensitive=True)  #접두사는 !, 대소문자 구분안함
slash = SlashCommand(bot, sync_commands=True, sync_on_cog_reload=True)

@bot.event
async def on_ready():#디버그 끝나면


    channel = bot.get_channel(960397196145078333)
    month = datetime.now().month
    day = datetime.now().day
    kstH = datetime.now().hour
    kstM = datetime.now().minute
    print("후.. 버그안났다")
    now_date = str(month) + '월' + str(day) + '일'
    now_time = str(kstH) + '시' + str(kstM) + '분'
    print(now_date)
    print(now_time)
    game = discord.Game("Star Citizen")
    await bot.change_presence(status=discord.Status.online, activity=game)


fleetColour = discord.Colour.dark_gold()#함대관련
introduceColour = discord.Colour.blurple()#안내
dicoColour = discord.Colour.blue()#디코 관련
albaColour = discord.Colour.gold()#알바 관련



for filename in os.listdir("Cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"Cogs.{filename[:-3]}")
for filename in os.listdir("Spread"):
    if filename.endswith(".py"):
        bot.load_extension(f"Spread.{filename[:-3]}")


@bot.command(name="리로드")
async def reload_commands(ctx, extension=None):
    if extension is None: # extension이 None이면 (그냥 !리로드 라고 썼을 때)
        for filename in os.listdir("Cogs"):
            if filename.endswith(".py"):
                bot.unload_extension(f"Cogs.{filename[:-3]}")
                bot.load_extension(f"Cogs.{filename[:-3]}")
                await ctx.send(":white_check_mark: 모든 명령어를 다시 불러왔습니다!")
    else:
        bot.unload_extension(f"Cogs.{extension}")
        bot.load_extension(f"Cogs.{extension}")
        await ctx.send(f":white_check_mark: {extension}을(를) 다시 불러왔습니다!")



@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title="에러!!", color=0xFF0000)
        embed.add_field(name=":warning:에러:warning: ", value="존재하지 않는 명령어입니다", inline=False)
        embed.add_field(name='문의',value="<@510802143654182913>")
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="에러!!", description="에러가 발생했습니다.", color=0xFF0000)
        embed.add_field(name="상세", value=f"```{error}```", inline=False)
        embed.add_field(name='문의', value="<@510802143654182913>")
        await ctx.send(embed=embed)

@bot.command()
async def 핑(ctx):
    latancy = bot.latency
    await ctx.send(str(round(latancy*1000,2))+'ms')

aegisColour = ShipContainer['aegisColour']
#로드맵
#dk 실험실
"""
1. 신규함선 추가 
2. 문자열 ', "",''를 -> '''로 변경x
3. 스프레드수정 및X 함수 추가
4. 환율에서 다양한 단위 추가 (연기)
5. 변수들 딕셔너리화X
6. 변수선언 간단하게X
7. 프리랜서미스 오류 12->13X
8. 디스코드에서 스프레드 수정 명령어 제작 
9. self함선명 스프레드 찾기(이상하게 안됨)
10. 번역기X
11. 무역 보조 프로그램제작
12. 하루마다 또는 특정한 기간마다 정보 업뎃 
"""


# 맨션
@bot.command()
async def DK(ctx):
    await ctx.send('<@510802143654182913>')

@bot.command(pass_context=True)
async def 봇수정(ctx):
    guild = ctx.guild
    if int(guild.id) == 960397196145078333:
        embed = discord.Embed(title='봇수정 링크입니다',
                              description='https://docs.google.com/spreadsheets/d/1qgehPVCUEf8ng-xRc9sRZxHwQe44CRvF69MBwO5XxG4/edit#gid=0',
                              colour=discord.Colour.blurple())
        embed.set_footer(text='Galaxy Cluster')
        await ctx.send(embed=embed)
    else:
        pass



bot.run("OTI0ODk4MDY4MjM3Nzk5NDg0.YclQcw.Pn_djOzaGPz-4iVOQcQt1gVScaE")