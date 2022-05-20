import discord             #디스코드 모듈
import asyncio             #아나시코 모듈
import random              #랜덤 모듈
import datetime            #시간 관련 모듈
import pytz                #
import urllib.request      #크롤링
import requests            #크롤링
import time
import math
import gspread
import os
import youtube_dl
import pandas as pd
import os
from FunctionFunction import *
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
from discord.ext import commands


bot=commands

class Utill(commands.Cog):

    def __init__(self,bot):
        self.bot=bot

    # 시차, 환율, 핑 (유틸리티)
    @bot.command()
    async def 시간(self, ctx):
        UTCH = datetime.datetime.now(timezone.utc).hour
        UTCM = datetime.datetime.now(timezone.utc).minute
        KSTH = UTCH + 9
        PSTH = UTCH + 16
        ESTH = UTCH + 19
        PSTHD = UTCH + 17
        ESTHD = UTCH + 20
        if KSTH >= 24:
            KSTH = KSTH - 24
        if PSTH >= 24:
            PSTH = PSTH - 24
        if ESTH >= 24:
            ESTH = ESTH - 24
        if PSTHD >= 24:
            PSTHD = PSTHD - 24
        if ESTHD >= 24:
            ESTHD = ESTHD - 24
        embed = discord.Embed(
            title='현재 세계 시간',
            description=("한국: " + str(KSTH) + "시 " + str(UTCM) + "분\n" +
                         "태평양: " + str(PSTH) + "시 " + str(UTCM) + "분\n" +
                         "미동부: " + str(ESTH) + "시 " + str(UTCM) + "분\n" +
                         "태평양일광: " + str(PSTHD) + "시 " + str(UTCM) + "분\n" +
                         "미동부일광: " + str(ESTHD) + "시 " + str(UTCM) + "분\n" +
                         "협정세계시: " + str(UTCH) + "시 " + str(UTCM) + "분\n"
                         ),
            colour=discord.Colour.blurple()
        )
        embed.set_footer(text='Galaxy Cluster')
        await ctx.send(embed=embed)

    @bot.command(pass_context=True)
    async def 환율(self, ctx, *refund):
        url = 'https://finance.naver.com/marketindex/exchangeDetail.nhn?marketindexCd=FX_USDKRW'
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        for x in range(0, 1):
            result = soup.select(
                "#container > div.aside > div:nth-child(2) > table > tbody > tr:nth-child(1) > td:nth-child(3)")[
                x].get_text()
        refund = list(refund)
        refund = "".join(refund)
        if refund:
            resultvalue = result[:-1]
            refund = list(refund)
            refund = "".join(refund)
            dalwon = refund[-1]
            refund = list(refund)
            del refund[-1]
            refund = "".join(refund)

            def refundus(resultvalue, refund, dalwon):
                resultvalue = "".join(resultvalue.split(","))
                number = refund
                cal = resultvalue + "*" + number
                resultre = eval(cal)
                resultre = round(resultre, 2)
                resultvat = round(eval(cal + "*1.1"), 2)
                embed = discord.Embed(title='환율',
                                      description='현재 달러 환율 : ' + str(result) + "\n환율 계산 값 : " + str(
                                          resultre) + "원\n" + "부가세를 포함한 환율 : " + str(resultvat) + '원\n',
                                      colour=discord.Colour.blurple())
                embed.set_image(
                    url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRpMcqFpJNCvZeaJ2x1BDDjNisQcHqBPW0ztw&usqp=CAU')
                embed.set_footer(text='신한은행 기준')
                ex_us = embed
                return ex_us

            def refundkr(resultvalue, refund, dalwon):
                resultvalue = "".join(resultvalue.split(","))
                number = refund
                cal = number + "/" + resultvalue
                resultre = eval(cal)
                resultre = round(resultre, 2)
                embed = discord.Embed(title='환율',
                                      description='현재 달러 환율 : ' + str(result) + "\n환율 계산 값 : " + str(
                                          resultre) + "원\n" + "부가세를 포함한 환율 : " + str(resultvat) + '원\n',
                                      colour=discord.Colour.blurple())
                embed.set_image(
                    url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRpMcqFpJNCvZeaJ2x1BDDjNisQcHqBPW0ztw&usqp=CAU')
                embed.set_footer(text='신한은행 기준')
                ex_kr = embed
                return ex_kr

            if dalwon == "불":
                embed = refundus(resultvalue, refund, dalwon)
                await ctx.send(embed=embed)
            elif dalwon == "원":
                embed = refundkr(resultvalue, refund, dalwon)
                await ctx.send(embed=embed)
            elif dalwon == "$":
                embed = refundus(resultvalue, refund, dalwon)
                await ctx.send(embed=embed)
            elif dalwon == "₩":
                embed = refundkr(resultvalue, refund, dalwon)
                await ctx.send(embed=embed)
            elif dalwon == "러":
                refund = list(refund)
                del refund[-1]
                refund = "".join(refund)
                resultvalue = "".join(resultvalue.split(","))
                number = refund
                cal = resultvalue + "*" + number
                resultre = eval(cal)
                resultre = round(resultre, 2)
                resultvat = round(eval(cal + "*1.1"), 2)
                embed = discord.Embed(title='환율',
                                      description='현재 달러 환율 : ' + str(result) + "\n환율 계산 값 : " + str(
                                          resultre) + "원\n" + "부가세를 포함한 환율 : " + str(resultvat) + '원\n',
                                      colour=discord.Colour.blurple())
                embed.set_image(
                    url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRpMcqFpJNCvZeaJ2x1BDDjNisQcHqBPW0ztw&usqp=CAU')
                embed.set_footer(text='신한은행 기준')

                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title='환율', description='현재 달러 환율 : ' + str(result),
                                      colour=discord.Colour.blurple())
            embed.set_image(
                url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRpMcqFpJNCvZeaJ2x1BDDjNisQcHqBPW0ztw&usqp=CAU')
            embed.set_footer(text='신한은행 기준')
            await ctx.send(embed=embed)

    @bot.command()
    async def 번역(self, ctx,  *, arg=None):
        arg = "".join(arg)
        trans = get_translate(arg)
        await ctx.send(trans)

def setup(bot):
    bot.add_cog(Utill(bot))