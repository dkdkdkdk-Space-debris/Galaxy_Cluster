from FunctionFunction import *

stantonColour = PlanetContainer['stantonColour']
hurColour = PlanetContainer['hurColour']
cruColour = PlanetContainer['cruColour']
arcColour = PlanetContainer['arcColour']
micColour = PlanetContainer['micColour']

class PlanetSystem(commands.Cog):

    def __init__(self,bot):
        self.bot=bot


    # 스탠턴
    stanton = "https://github.com/trashstarfleet/trahbot/blob/main/stanton"

    @bot.command(pass_context=True)
    async def 스탠턴(self, ctx):
        await ctx.send(embed=planetFunction(3,'STANTON', stantonColour))

    # 허스턴
    @bot.command(pass_context=True)
    async def 허스턴(self, ctx):
        await ctx.send(embed=planetFunction(4,'STANTON', hurColour))

    @bot.command(pass_context=True)
    async def 로어빌(self, ctx):
        await ctx.send(embed=cityFunction(5,'STANTON', hurColour))

    @bot.command(pass_context=True)
    async def 에버러스하버(self, ctx):
        await ctx.send(embed=subFunction(6,'STANTON', hurColour))

    @bot.command(pass_context=True)
    async def 에버루스하버(self, ctx):
        await ctx.send(embed=subFunction(6,'STANTON', hurColour))

    @bot.command(pass_context=True)
    async def 에버러스(self, ctx, *everus):
        everus = "".join(everus)
        if everus == "하버":
            await ctx.send(embed=subFunction(6,'STANTON', hurColour))

    @bot.command(pass_context=True)
    async def 에버루스(self, ctx, *everus):
        everus = "".join(everus)
        if everus == "하버":
            await ctx.send(embed=subFunction(6,'STANTON', hurColour))

    @bot.command(pass_context=True)
    async def 에리얼(self, ctx):
        await ctx.send(embed=planetFunction(7,'STANTON', hurColour))

    @bot.command(pass_context=True)
    async def 에버딘(self, ctx):
        await ctx.send(embed=planetFunction(8,'STANTON', hurColour))

    @bot.command(pass_context=True)
    async def 감옥(self, ctx):
        await ctx.send(embed=subFunction(9,'STANTON', hurColour))

    @bot.command(pass_context=True)
    async def 탈옥(self, ctx):
        await ctx.send(embed=subFunction(9,'STANTON', hurColour))

    @bot.command(pass_context=True)
    async def 클레셔재활시설(self, ctx):
        await ctx.send(embed=subFunction(9,'STANTON', hurColour))

    @bot.command(pass_context=True)
    async def 클레셔(self, ctx, **jail):
        await ctx.send(embed=subFunction(9,'STANTON', hurColour))

    @bot.command(pass_context=True)
    async def 이타(self, ctx):
        await ctx.send(embed=planetFunction(10,'STANTON', hurColour))

    @bot.command(pass_context=True)
    async def 마그다(self, ctx):
        await ctx.send(embed=planetFunction(11,'STANTON', hurColour))

    # 크루세이더
    @bot.command(pass_context=True)
    async def 크루세이더(self, ctx):
        await ctx.send(embed=planetFunction(12,'STANTON', cruColour))

    @bot.command(pass_context=True)
    async def 오리슨(self, ctx):
        await ctx.send(embed=cityFunction(13, 'STANTON', cruColour))

    @bot.command(pass_context=True)
    async def 오리즌(self, ctx):
        await ctx.send(embed=cityFunction(13, 'STANTON', cruColour))

    @bot.command(pass_context=True)
    async def 포트올리사(self, ctx):
        await ctx.send(embed=subFunction(14,'STANTON', cruColour))

    @bot.command(pass_context=True)
    async def 포트(self, ctx, *olisa):
        olisa = "".join(olisa)
        if olisa == '올리사':
            await ctx.send(embed=subFunction(14,'STANTON', cruColour))
        elif olisa == '트레슬러':
            await ctx.send(embed=subFunction(26,'STANTON', micColour))

    @bot.command(pass_context=True)
    async def po(self, ctx):
        await ctx.send(embed=subFunction(14,'STANTON', cruColour))

    @bot.command(pass_context=True)
    async def 셀린(self, ctx):
        await ctx.send(embed=planetFunction(15,'STANTON', cruColour))

    @bot.command(pass_context=True)
    async def 데이머(self, ctx):
        await ctx.send(embed=planetFunction(16,'STANTON', cruColour))

    @bot.command(pass_context=True)
    async def 데이마르(self, ctx):
        await ctx.send(embed=planetFunction(16,'STANTON', cruColour))

    @bot.command(pass_context=True)
    async def 옐라(self, ctx):
        await ctx.send(embed=planetFunction(17,'STANTON', cruColour))

    @bot.command(pass_context=True)
    async def 그림헥스(self, ctx):
        await ctx.send(embed=subFunction(18,'STANTON', cruColour))

    @bot.command(pass_context=True)
    async def 그림(self, ctx, *hex):
        hex = "".join(hex)
        print(hex)
        if hex == '헥스':
            await ctx.send(embed=subFunction(18,'STANTON', cruColour))

    @bot.command(pass_context=True)
    async def 그헥(self, ctx):
        await ctx.send(embed=subFunction(18,'STANTON', cruColour))

    # 아크콥
    @bot.command(pass_context=True)
    async def 아크콥(self, ctx):
        await ctx.send(embed=planetFunction(19,'STANTON', arcColour))

    @bot.command(pass_context=True)
    async def 에리어18(self, ctx):
        await ctx.send(embed=cityFunction(20,'STANTON', arcColour))

    @bot.command(pass_context=True)
    async def 에리어(self, ctx, *area):
        area = "".join(area)
        if area == '18':
            await ctx.send(embed=cityFunction(20,'STANTON', arcColour))

    @bot.command(pass_context=True)
    async def 에어리어18(self, ctx):
        await ctx.send(embed=cityFunction(20,'STANTON', arcColour))

    @bot.command(pass_context=True)
    async def 에어리어(self, ctx, *area):
        area = "".join(area)
        if area == '18':
            await ctx.send(embed=cityFunction(20,'STANTON', arcColour))

    @bot.command(pass_context=True)
    async def 바이지니포인트(self, ctx):
        await ctx.send(embed=subFunction(21,'STANTON', arcColour))

    @bot.command(pass_context=True)
    async def 바이지니(self, ctx, *baijini):
        baijini = "".join(baijini)
        if baijini == '포인트':
            await ctx.send(embed=subFunction(21,'STANTON', arcColour))

    @bot.command(pass_context=True)
    async def 릴리아(self, ctx):
        await ctx.send(embed=planetFunction(22,'STANTON', arcColour))

    @bot.command(pass_context=True)
    async def 라이리아(self, ctx):
        await ctx.send(embed=planetFunction(22,'STANTON', arcColour))

    @bot.command(pass_context=True)
    async def 왈라(self, ctx):
        await ctx.send(embed=planetFunction(23,'STANTON', arcColour))

    # 마이크로텍
    @bot.command(pass_context=True)
    async def 마이크로텍(self, ctx):
        await ctx.send(embed=planetFunction(24,'STANTON', micColour))

    @bot.command(pass_context=True)
    async def 마텍(self, ctx):
        await ctx.send(embed=planetFunction(24,'STANTON', micColour))

    @bot.command(pass_context=True)
    async def 뉴배비지(self, ctx):
        await ctx.send(embed=cityFunction(25,'STANTON', micColour))

    @bot.command(pass_context=True)
    async def 뉴베비지(self, ctx):
        await ctx.send(embed=cityFunction(25,'STANTON', micColour))

    @bot.command(pass_context=True)
    async def 뉴배버지(self, ctx):
        await ctx.send(embed=cityFunction(25,'STANTON', micColour))

    @bot.command(pass_context=True)
    async def 뉴베버지(self, ctx):
        await ctx.send(embed=cityFunction(25,'STANTON', micColour))

    @bot.command(pass_context=True)
    async def 뉴(self, ctx, *babbage):
        babbage = "".join(babbage)
        if babbage == '배비지':
            await ctx.send(embed=cityFunction(25,'STANTON', micColour))
        elif babbage == "베비지":
            await ctx.send(embed=cityFunction(25,'STANTON', micColour))
        elif babbage == "배버지":
            await ctx.send(embed=cityFunction(25,'STANTON', micColour))
        elif babbage == "베버지":
            await ctx.send(embed=cityFunction(25,'STANTON', micColour))
        else:
            await ctx.send(embed=cityFunction(25,'STANTON', micColour))

    @bot.command(pass_context=True)
    async def 포트트레슬러(self, ctx):
        await ctx.send(embed=subFunction(26, 'STANTON', micColour))

    @bot.command(pass_context=True)
    async def 칼리오페(self, ctx):
        await ctx.send(embed=planetFunction(27,'STANTON', micColour))

    @bot.command(pass_context=True)
    async def 사일로(self, ctx):
        await ctx.send(embed=planetFunction(28,'STANTON', micColour))

    @bot.command(pass_context=True)
    async def 유터페(self, ctx):
        await ctx.send(embed=planetFunction(29,'STANTON', micColour))



'''

돌아올때까지 보류 
닉스 안녕~~~
    # nyx행성계
    nyx = "https://github.com/trashstarfleet/trashbot/blob/main/nyx"

    @bot.command(pass_context=True)
    async def 델라마(self, ctx):
        await ctx.send(embed=planetFunction(nyx, delamaColour, *Listprocess(25, 30)))

    @bot.command(pass_context=True)
    async def 델라마르(self, ctx):
        await ctx.send(embed=planetFunction(nyx, delamaColour, *Listprocess(25, 30)))

    @bot.command(pass_context=True)
    async def 레브스키(self, ctx):
        await ctx.send(embed=cityFunction(nyx, delamaColour, *Listprocess(55, 55)))

    @bot.command(pass_context=True)
    async def 렙스키(self, ctx):
        await ctx.send(embed=cityFunction(nyx, delamaColour, *Listprocess(55, 55)))
'''
def setup(bot):
    bot.add_cog(PlanetSystem(bot))