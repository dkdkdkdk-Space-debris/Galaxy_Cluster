from FunctionFunction import *
from discord.ext import commands
from discord_slash import cog_ext, SlashContext


esperiaColour = ShipContainer['esperiaColour']
vandulColour = ShipContainer['vandulColour']
aopoaColour = ShipContainer['aopoaColour']
banuColour = ShipContainer['banuColour']

class ALIEN(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name='글레이브', description='세부함선 없음',guild_ids=[960397196145078333])
    async def _글레이브(self, ctx):
        await ctx.send(embed=shipFunction(3, '외계인', esperiaColour))
    @bot.command(pass_context=True)
    async def 글레이브(self, ctx):
        await ctx.send(embed=shipFunction(3, '외계인', esperiaColour))

    @bot.command(pass_context=True)
    async def 블레이드(self, ctx):
        await ctx.send(embed=shipFunction(4, '외계인', esperiaColour))

    @bot.command(pass_context=True)
    async def 탈론(self, ctx, *talon):
        talon = list(talon)
        talon = "".join(talon)
        if talon == "쉬릭":
            await ctx.send(embed=shipFunction(6, '외계인', esperiaColour))
        elif talon == "쉬라이크":
            await ctx.send(embed=shipFunction(6, '외계인', esperiaColour))
        else:
            await ctx.send(embed=shipFunction(5, '외계인', esperiaColour))

    @bot.command(pass_context=True)
    async def 탈론쉬릭(self, ctx):
        await ctx.send(embed=shipFunction(6, '외계인', esperiaColour))

    @bot.command(pass_context=True)
    async def 탈론쉬라이크(self, ctx):
        await ctx.send(embed=shipFunction(6, '외계인', esperiaColour))

    @bot.command(pass_context=True)
    async def 쉬라이크(self, ctx):
        await ctx.send(embed=shipFunction(6, '외계인', esperiaColour))

    @bot.command(pass_context=True)
    async def 쉬릭(self, ctx):
        await ctx.send(embed=shipFunction(6, '외계인', esperiaColour))

    @bot.command(pass_context=True)
    async def 프라울러(self, ctx):
        await ctx.send(embed=shipFunction(7, '외계인', esperiaColour))

    @bot.command(pass_context=True)
    async def 사이드(self, ctx):
        await ctx.send(embed=shipFunction(27, '외계인', vandulColour))


#시안 아오포아 가탁
    @bot.command(pass_context=True)
    async def 샨톡아이(self, ctx):
        await ctx.send(embed=shipFunction(12, '외계인', aopoaColour))

    @bot.command(pass_context=True)
    async def 샨토카이(self, ctx):
        await ctx.send(embed=shipFunction(12, '외계인', aopoaColour))

    @bot.command(pass_context=True)
    async def 산토끼(self, ctx):
        await ctx.send(embed=shipFunction(12, '외계인', aopoaColour))

    @bot.command(pass_context=True)
    async def 카투알(self, ctx):
        await ctx.send(embed=shipFunction(10, '외계인', aopoaColour))

    @bot.command(pass_context=True)
    async def 퀴어칼투(self, ctx):
        await ctx.send(embed=shipFunction(11, '외계인', aopoaColour))

    @bot.command(pass_context=True)
    async def 레일렌(self, ctx):
        await ctx.send(embed=shipFunction(28, '외계인', vandulColour))

    @bot.command(pass_context=True)
    async def 녹스쿠에(self, ctx):
        await ctx.send(embed=shipFunction(27, '외계인', aopoaColour))

    @bot.command(pass_context=True)
    async def 녹스(self, ctx):
        await ctx.send(embed=shipFunction(13, '외계인', aopoaColour))



#바누
    @bot.command(pass_context=True)
    async def 바누(self, ctx, *banu):
        if banu == "디펜더":
            await ctx.send(embed=shipFunction(8, '외계인', banuColour))
        else:
            await ctx.send(embed=speciesFunction(4, '종족', banuColour))

    @bot.command(pass_context=True)
    async def 디펜더(self, ctx):
        await ctx.send(embed=shipFunction(8, '외계인', banuColour))

    @bot.command(pass_context=True)
    async def 바누디펜더(self, ctx):
        await ctx.send(embed=shipFunction(8, '외계인', banuColour))

    @bot.command(pass_context=True)
    async def 머천트맨(self, ctx):
        await ctx.send(embed=shipFunction(9, '외계인', banuColour))


#반둘
    @bot.command(pass_context=True)
    async def 킹쉽(self, ctx):
        await ctx.send(embed=shipFunction(14, '외계인', vandulColour))

    @bot.command(pass_context=True)
    async def 클레버(self, ctx):
        await ctx.send(embed=shipFunction(15, '외계인', vandulColour))

    @bot.command(pass_context=True)
    async def 크롤러(self, ctx):
        await ctx.send(embed=shipFunction(16, '외계인', vandulColour))

    @bot.command(pass_context=True)
    async def 드릴러(self, ctx):
        await ctx.send(embed=shipFunction(17, '외계인', vandulColour))

    @bot.command(pass_context=True)
    async def 하베스터(self, ctx):
        await ctx.send(embed=shipFunction(19, '외계인', vandulColour))

    @bot.command(pass_context=True)
    async def 하베스터캐리어(self, ctx):
        await ctx.send(embed=shipFunction(18, '외계인', vandulColour))

    @bot.command(pass_context=True)
    async def 해칫(self, ctx):
        await ctx.send(embed=shipFunction(20, '외계인', vandulColour))

    @bot.command(pass_context=True)
    async def 헌터(self, ctx):
        await ctx.send(embed=shipFunction(21, '외계인', vandulColour))

    @bot.command(pass_context=True)
    async def 라이트파이어(self, ctx):
        await ctx.send(embed=shipFunction(22, '외계인', vandulColour))

    @bot.command(pass_context=True)
    async def 몰러(self, ctx):
        await ctx.send(embed=shipFunction(23, '외계인', vandulColour))

    @bot.command(pass_context=True)
    async def 스팅어(self, ctx):
        await ctx.send(embed=shipFunction(24, '외계인', vandulColour))

    @bot.command(pass_context=True)
    async def 토마호크(self, ctx):
        await ctx.send(embed=shipFunction(25, '외계인', vandulColour))

    @bot.command(pass_context=True)
    async def 보이드(self, ctx):
        await ctx.send(embed=shipFunction(26, '외계인', vandulColour))


def setup(bot):
    bot.add_cog(ALIEN(bot))