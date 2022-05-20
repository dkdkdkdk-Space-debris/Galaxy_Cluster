
from FunctionFunction import *


class HP(commands.Cog):

    def __init__(self,bot):
        self.bot=bot

    @bot.command(pass_context=True)
    async def 부품(self, ctx, *arg):
        arg = "".join(arg)
        if arg == "":
            embed = discord.Embed(title='부품', description='함선 부품은 크게 퀀텀드라이브(!퀀텀), 파워플랜트(!파워), 쉴드 제너레이터(!쉴드), 쿨러(!쿨러)로 나누어져 있습니다.\n'
                                                          '사이즈 별로 0(차량), 1(소형 S), 2(중형 M), 3(대형 L), 4(캐피탈)로사이즈로 나뉘고\n'
                                                          '용도에 따라 군용(!군용), 민간(!민간), 산업(!산업), 스텔스(!스텔스), 경기용(!경기용)으로 나뉘어집니다.\n'
                                                          '또한  등급에 따라 A, B, C, D로 나누어 지고 A로 갈수록 좋은 부품입니다.', colour=discord.Colour.blue())
            embed.add_field(name='**!부품 사용법**', value='!부품을 치시고 뒤에\n구체적인 부품명을 적어 주시면 됩니다.\n예시) !부품 XL-1 !부품 xl-1\n!부품 티에스투 !부품 선파이어\n구체적인 부품명은 !퀀텀 !쉴드\n등으로 찾을수있습니다', inline=True)
            embed.add_field(name='**!퀀텀, !파워, !쉴드, !쿨러 사용법**', value='간단히 위 명령어를 치시면 부품 설명과 사용법이 나옵니다.', inline=True)
            embed.set_footer(text='Galaxy Cluster')
            await ctx.send(embed=embed)
        else:
            ws = ss.worksheet('component')
            raw = str(ws.find(arg).row)
            await ctx.send(embed=HardPoint_Function(raw, 'component'))

    @bot.command(pass_context=True)
    async def 군용(self, ctx):
        await ctx.send(embed=ComIntroFunction(2, 'intro'))
    @bot.command(pass_context=True)
    async def 민간(self, ctx):
        await ctx.send(embed=ComIntroFunction(3, 'intro'))
    @bot.command(pass_context=True)
    async def 산업(self, ctx):
        await ctx.send(embed=ComIntroFunction(4, 'intro'))
    @bot.command(pass_context=True)
    async def 스텔스(self, ctx):
        await ctx.send(embed=ComIntroFunction(5, 'intro'))
    @bot.command(pass_context=True)
    async def 경기용(self, ctx):
        await ctx.send(embed=ComIntroFunction(6, 'intro'))

    @bot.command(pass_context=True)
    async def 퀀텀(self, ctx, *arg):

        arg = "".join(arg)
        link = 'component'
        rangeName = 'A3:A58'
        rangeClass = 'C3:C58'
        rangeGrade = 'E3:E58'
        title = '퀀텀 드라이브 목록'
        image = 'https://cig-galactapedia-prod.s3.amazonaws.com/upload/8397d8c8-5c00-49af-87d8-3e18ee65f816'
        if arg =='1사이즈':
            title='1사이즈 '+title
            rangeName = 'A3:A22'
            rangeClass = 'C3:C22'
            rangeGrade = 'E3:E22'
            await ctx.send(embed=ComponentDetailFunction(link,rangeName,rangeClass,rangeGrade, title, image))
        elif arg =='2사이즈':
            title = '2사이즈 ' + title
            rangeName = 'A23:A42'
            rangeClass = 'C23:C42'
            rangeGrade = 'E23:E42'
            await ctx.send(embed=ComponentDetailFunction(link,rangeName,rangeClass,rangeGrade, title, image))
        elif arg =='3사이즈':
            title = '3사이즈 ' + title
            rangeName = 'A43:A57'
            rangeClass = 'C433:C57'
            rangeGrade = 'E43:E57'
            await ctx.send(embed=ComponentDetailFunction(link,rangeName,rangeClass,rangeGrade, title, image))
        elif arg == '목록':
            await ctx.send(embed=ComponentDetailFunction(link,rangeName,rangeClass,rangeGrade, title, image))
        elif arg == '드라이브':
            await ctx.send(embed=ComIntroFunction(8, 'intro'))
        else:
            await ctx.send(embed=ComIntroFunction(8, 'intro'))
    @bot.command(pass_context=True)
    async def 쉴드(self, ctx, *arg):
        ws = ss.worksheet('component')
        arg = "".join(arg)
        link = 'component'
        rangeName = 'A60:A122'
        rangeClass = 'C60:C122'
        rangeGrade = 'E60:E122'
        title = '쉴드 제너레이터 목록'
        image = 'https://static.wikia.nocookie.net/starcitizen/images/9/95/Shield_generator.jpg/revision/latest/scale-to-width-down/1000?cb=20200528174534'
        if arg == '1사이즈':
            title = '1사이즈 ' + title
            rangeName = 'A62:A84'
            rangeClass = 'C62:C84'
            rangeGrade = 'E62:E84'
            await ctx.send(embed=ComponentDetailFunction(link,rangeName,rangeClass,rangeGrade, title, image))
        elif arg == '2사이즈':
            title = '2사이즈 ' + title
            rangeName = 'A85:A107'
            rangeClass = 'C85:C107'
            rangeGrade = 'E85:E107'
            await ctx.send(embed=ComponentDetailFunction(link,rangeName,rangeClass,rangeGrade, title, image))
        elif arg == '3사이즈':
            title = '3사이즈 ' + title
            rangeName = 'A108:A121'
            rangeClass = 'C108:C121'
            rangeGrade = 'E108:E121'
            await ctx.send(embed=ComponentDetailFunction(link,rangeName,rangeClass,rangeGrade, title, image))
        elif arg == '목록':
            await ctx.send(embed=ComponentDetailFunction(link,rangeName,rangeClass,rangeGrade, title, image))
        elif arg == '제너레이터':
            await ctx.send(embed=ComIntroFunction(9, 'intro'))
        else:
            await ctx.send(embed=ComIntroFunction(9, 'intro'))
    @bot.command(pass_context=True)
    async def 쿨러(self, ctx, *arg):
        ws = ss.worksheet('component')
        arg = "".join(arg)
        link = 'component'
        rangeName = 'A124:A193'
        rangeClass = 'C124:C193'
        rangeGrade = 'E124:E193'
        title = '쿨러 목록'
        image = 'https://static.wikia.nocookie.net/starcitizen/images/6/6d/Coolers.jpg/revision/latest/scale-to-width-down/1000?cb=20200528174535'
        if arg == '1사이즈':
            title = '1사이즈 ' + title
            rangeName = 'A130:A152'
            rangeClass = 'C130:C152'
            rangeGrade = 'E130:E152'
            await ctx.send(embed=ComponentDetailFunction(link,rangeName,rangeClass,rangeGrade, title, image))
        elif arg == '2사이즈':
            title = '2사이즈 ' + title
            rangeName = 'A153:A175'
            rangeClass = 'C153:C175'
            rangeGrade = 'E153:E175'
            await ctx.send(embed=ComponentDetailFunction(link,rangeName,rangeClass,rangeGrade, title, image))
        elif arg == '3사이즈':
            title = '3사이즈 ' + title
            rangeName = 'A176:A192'
            rangeClass = 'C176:C192'
            rangeGrade = 'E176:E192'
            await ctx.send(embed=ComponentDetailFunction(link,rangeName,rangeClass,rangeGrade, title, image))
        elif arg == '목록':
            await ctx.send(embed=ComponentDetailFunction(link,rangeName,rangeClass,rangeGrade, title, image))
        else:
            await ctx.send(embed=ComIntroFunction(10, 'intro'))
    @bot.command(pass_context=True)
    async def 파워(self, ctx, *arg):
        ws = ss.worksheet('component')
        arg = "".join(arg)
        link = 'component'
        rangeName = 'A195:A267'
        rangeClass = 'C195:C267'
        rangeGrade = 'E195:E267'
        title = '파워 플랜트 목록'
        image = 'https://static.wikia.nocookie.net/starcitizen/images/e/e0/Power_plant.jpg/revision/latest/scale-to-width-down/2000?cb=20200528174536'
        if arg == '1사이즈':
            title = '1사이즈 ' + title
            rangeName = 'A201:A224'
            rangeClass = 'C201:C224'
            rangeGrade = 'E201:E224'
            await ctx.send(embed=ComponentDetailFunction(link,rangeName,rangeClass,rangeGrade, title, image))
        elif arg == '2사이즈':
            title = '2사이즈 ' + title
            rangeName = 'A225:A248'
            rangeClass = 'C225:C248'
            rangeGrade = 'E225:E248'
            await ctx.send(embed=ComponentDetailFunction(link,rangeName,rangeClass,rangeGrade, title, imagee))
        elif arg == '3사이즈':
            title = '3사이즈 ' + title
            rangeName = 'A249:A265'
            rangeClass = 'C249:C265'
            rangeGrade = 'E249:E265'
            await ctx.send(embed=ComponentDetailFunction(link,rangeName,rangeClass,rangeGrade, title, image))
        elif arg == '목록':
            await ctx.send(embed=ComponentDetailFunction(link,rangeName,rangeClass,rangeGrade, title, image))
        elif arg == '플랜트':
            await ctx.send(embed=ComIntroFunction(11, 'intro'))
        else:
            await ctx.send(embed=ComIntroFunction(11, 'intro'))

def setup(bot):
    bot.add_cog(HP(bot))