import discord
import gspread
import asyncio
import os
import sys
import urllib.request
import requests
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from discord.ext import commands
from discord.ext.commands import Bot
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import  create_choice, create_option

bot = Bot(command_prefix='!', intents=discord.Intents.all(), strip_after_prefix=False, case_insensitive=True)
icon = 'https://wallpaperaccess.com/full/96613.jpg'#아이콘 이미지
#함선 제조사
ShipContainer = {'aegisColour'   :discord.Colour.dark_grey(),   'esperiaColour'  :discord.Colour.darker_grey(),
                 'aopoaColour'   :discord.Colour.green(),       'banuColour'     :discord.Colour.dark_gold(),
                 'vandulColour'  :discord.Colour.dark_teal(),   'anvilColour'    :discord.Colour.light_grey(),
                 'argoColour'    :discord.Colour.dark_orange(), 'tumbrilColour'  :discord.Colour.dark_green(),
                 'cnouColour'    :discord.Colour.dark_blue(),   'crusaderColour' :discord.Colour.greyple(),
                 'drakeColour'   :discord.Colour.dark_red(),    'krugerColour'   :discord.Colour.red(),
                 'greycatColour' :discord.Colour.teal(),        'miscColour'     :discord.Colour.lighter_grey(),
                 'originColour'  :discord.Colour.blue(),        'rsiColour'      :discord.Colour.orange()}

SubContainer = {'introduceColour' :discord.Colour.blurple(), 'dicoColour' :discord.Colour.blue()}

#행성
PlanetContainer = {'stantonColour' :discord.Colour.orange(),  'hurColour'    :discord.Colour.dark_orange(),
                   'cruColour'     :discord.Colour.magenta(), 'poColour'     :discord.Colour.gold(),
                   'grimhexColour' :discord.Colour.red(),     'arcColour'    :discord.Colour.dark_red(),
                   'micColour'     :discord.Colour.blurple(), 'delamaColour' :discord.Colour.dark_grey()}
#종족
SpecisColour = {'aopoaColour' :discord.Colour.green(), 'banuColour' :discord.Colour.dark_gold(), 'vandulColour' :discord.Colour.dark_teal()}

#########################################################################################################################
bot=commands

#스프레드
scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']#주소?
folder= os.path.dirname(os.path.abspath(__file__))
file = os.path.join(folder, 'Spread/redcomet-338205-d825b8725833.json')#키인증
credentials = ServiceAccountCredentials.from_json_keyfile_name(file, scope)
gc = gspread.authorize(credentials)
ss = gc.open('Galaxy-Cluster ')

#함선


def shipFunction(input, worksheet, colour):
    ws = ss.worksheet(worksheet)
    inputData = ws.row_values(input)
    data = [None] * 19
    for num in range(1, 17):
        data[num] = "".join(inputData[num])
    embed = discord.Embed(title=data[1],url= data[15] , description=data[2], colour=colour)
    embed.set_image(url=data[3])
    embed.set_thumbnail(url=data[4])
    embed.add_field(name='''**제조사**''', value=data[5], inline=True)
    embed.add_field(name='''**분류**''', value=data[6], inline=True)
    embed.add_field(name='''**개발상태**''', value=data[7], inline=True)
    embed.add_field(name='''**전장/전폭/전고**''', value=data[8], inline=True)
    embed.add_field(name='''**중량**''', value=data[9], inline=True)
    embed.add_field(name='''**카고**''', value=data[10], inline=True)
    embed.add_field(name='''**순항속도**''', value=data[11], inline=True)
    embed.add_field(name='''**최소/최대 승무원**''', value=data[12], inline=True)
    embed.add_field(name='''**인게임 가격**''', value=data[13], inline=True)
    embed.add_field(name='''**파는곳**''', value=data[14], inline=True)
    embed.add_field(name='''**가격 VAT 별도**''', value=data[16], inline=True)
    embed.set_footer(text='Galaxy Cluster')
    return embed

def serisFunction(input,worksheet,colour):
    ws = ss.worksheet(worksheet)
    inputData = ws.row_values(input)
    data = [None] * 7
    for num in range(1, 5):
        result[num] = "".join(inputData[num])
    embed = discord.Embed(title=result[1],description=result[2],colour=colour)
    embed.set_image(url=result[3])
    embed.set_thumbnail(url=result[4])
    embed.set_footer(text='Galaxy Cluster')
    return embed

#기업
def companyFunction(input,worksheet):
    ws = ss.worksheet(worksheet)
    inputData = ws.row_values(input)
    data = [None] * 6
    for num in range(1, 4):
        result[num] = "".join(inputData[num])
    embed = discord.Embed(title=result[1],description=result[2],colour=discord.Colour.blurple())
    embed.set_image(url=result[3])
    embed.set_footer(text='Galaxy Cluster')
    return embed
#행성
def planetFunction(input, worksheet, colour):
    ws = ss.worksheet(worksheet)
    inputData = ws.row_values(input)
    data = [None] * 8
    for num in range(1, 6):
        data[num] = "".join(inputData[num])
    embed = discord.Embed(title=data[1],description=data[2],colour=colour)
    embed.set_image(url=data[3])
    embed.add_field(name=data[4], value=data[5],inline=True)
    embed.set_footer(text='Galaxy Cluster')
    return embed
#도시
def cityFunction(input, worksheet, colour):
    ws = ss.worksheet(worksheet)
    inputData = ws.row_values(input)
    data = [None] * 8
    for num in range(1, 6):
        result[num] = "".join(inputData[num])
    embed = discord.Embed(title=result[1],description=result[2],colour=colour)
    embed.set_image(url=result[3])
    embed.add_field(name='''먹을곳''', value=result[4], inline=True)
    embed.add_field(name='''퀀텀가능고도''', value=result[5], inline=True)
    embed.set_footer(text='Galaxy Cluster')
    return embed

def subFunction(input, worksheet, colour):
    ws = ss.worksheet(worksheet)
    inputData = ws.row_values(input)
    data = [None] * 6
    for num in range(1, 4):
        result[num] = "".join(inputData[num])
    embed = discord.Embed(title=result[1],description=result[2],colour=colour)
    embed.set_image(url=result[3])
    embed.set_footer(text='Galaxy Cluster')
    return embed

#함선 부품
def HardPoint_Function(input,worksheet):
    ws = ss.worksheet(worksheet)
    inputData = ws.row_values(input)
    data = [None] * 9
    for num in range(0, 7):
        data[num] = "".join(inputData[num])
    embed = discord.Embed(title=data[0],colour=discord.Colour.dark_grey())
    embed.add_field(name='''**제조사**''', value=data[1], inline=True)
    embed.add_field(name='''**분류**''', value=data[2], inline=True)
    embed.add_field(name='''**사이즈**''', value=data[3]+'사이즈', inline=True)
    embed.add_field(name='''**등급**''', value=data[4], inline=True)
    embed.add_field(name='''**파는곳**''', value=data[5], inline=True)
    embed.add_field(name='''**가격 **''', value=data[6]+'⍺UEC', inline=True)
    embed.set_footer(text='Galaxy Cluster')
    return embed

def ComponentDetailFunction(link, rangename, rangclass, rangegrade, title, image):
    ws = ss.worksheet(link)
    counter = 0
    rangename_list = ws.range(rangename)
    rangeclass_list = ws.range(rangclass)
    rangegrade_list = ws.range(rangegrade)
    desname = title[:-3] + '에는'
    desclass = [''] * 100
    desgrade = [''] * 100
    for cellclass in rangeclass_list:
        desclass[counter]=cellclass.value
        counter = counter + 1
    counter = 0
    for cellgrade in rangegrade_list:
        desgrade[counter]=cellgrade.value
        counter = counter + 1
    counter=0
    for cellname in rangename_list:
        desname = desname + " " + cellname.value + '('+desclass[counter]+' '+desgrade[counter]+'), '
        counter = counter + 1

    embed = discord.Embed(title=title, description='**' + desname + '가 있습니다' + '**', colour=discord.Colour.light_grey())
    embed.set_image(url=image)
    embed.set_footer(text='Galaxy Cluster')
    return embed
#무기
def WeaponFunction(input,worksheet):
    ws = ss.worksheet(worksheet)
    inputData = ws.row_values(input)
    data =  [None] * 16
    for num in range(0, 14):
        data[num] = "".join(inputData[num])
    embed = discord.Embed(title=data[0],colour=discord.Colour.dark_grey())
    embed.set_image(url=data[13])
    embed.add_field(name='''**제조사**''', value=data[1], inline=True)
    embed.add_field(name='''**분류**''', value=data[2], inline=True)
    embed.add_field(name='''**사이즈**''', value=data[3]+' 사이즈', inline=True)
    embed.add_field(name='''**DPS**''', value=data[4], inline=True)
    embed.add_field(name='''**알파 데미지**''', value=data[5], inline=True)
    embed.add_field(name='''**최소 폭발반경**''', value=data[6], inline=True)
    embed.add_field(name='''**최대 폭발 반경**''', value=data[7], inline=True)
    embed.add_field(name='''**연사력**''', value=data[8], inline=True)
    embed.add_field(name='''**사거리**''', value=data[9], inline=True)
    embed.add_field(name='''**발사 속도**''', value=data[10], inline=True)
    embed.add_field(name='''**탄약수**''', value=data[11], inline=True)
    embed.add_field(name='''**가격 **''', value=data[12] + '⍺UEC', inline=True)
    embed.set_footer(text='Galaxy Cluster')
    return embed

def MissileFunction(input,worksheet):
    ws = ss.worksheet(worksheet)
    inputData = ws.row_values(input)
    data = [None] * 9
    for num in range(0, 7):
        data[num] = "".join(inputData[num])
    embed = discord.Embed(title=data[0],colour=discord.Colour.dark_grey())
    embed.add_field(name='''**제조사**''', value=data[1], inline=True)
    embed.add_field(name='''**추적 방식**''', value=data[2], inline=True)
    embed.add_field(name='''**타입**''', value=data[3], inline=True)
    embed.add_field(name='''**사이즈**''', value=data[4]+' 사이즈', inline=True)
    embed.add_field(name='''**총 데미지**''', value=data[5], inline=True)
    embed.add_field(name='''**가격 **''', value=data[6] + ' ⍺UEC', inline=True)
    embed.set_footer(text='Galaxy Cluster')
    return embed

#설명
def ComIntroFunction(input,worksheet):
    ws = ss.worksheet(worksheet)
    inputData = ws.row_values(input)
    data =  [None] * 6
    for num in range(0, 4):
        data[num] = "".join(inputData[num])
    embed = discord.Embed(title=data[0], description=data[1],colour=discord.Colour.greyple())
    embed.set_image(url=data[2])
    embed.set_footer(text=data[3])
    embed.add_field(name='''**사용법**''', value=' !쿨러 목록 -> 쿨러 전체목록 !쿨러 n사이즈- > 사이즈별 목록', inline=True)
    embed.set_footer(text='Galaxy Cluster')
    return embed


#번역
def get_translate(text):
    client_id = "92skNl7L4kpvF_kLpp5N"  # 개발자센터에서 발급받은 Client ID 값
    client_secret = "rwm3UHqxE5" # <-- client_secret 기입

    encQuery = urllib.parse.quote(text)
    data = "query=" + encQuery
    url = "https://openapi.naver.com/v1/papago/detectLangs"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    if (rescode == 200):
        response_body = response.read()
        langCode = response_body.decode()
        langCode = langCode[13:15]

    else:
        print("Error Code:" + rescode)

    if langCode == 'en':
        transcode = 'ko'

    elif langCode == 'ko':
        transcode = 'en'
    else:
        print('error!')

    data = {'text' : text,
            'source' : langCode,
            'target': transcode}

    url = "https://openapi.naver.com/v1/papago/n2mt"

    header = {"X-Naver-Client-Id":client_id,
              "X-Naver-Client-Secret":client_secret}

    response = requests.post(url, headers=header, data=data)
    rescode = response.status_code

    if(rescode==200):
        send_data = response.json()
        trans_data = (send_data['message']['result']['translatedText'])
        return trans_data
    else:
        print("Error Code:" , rescode)
