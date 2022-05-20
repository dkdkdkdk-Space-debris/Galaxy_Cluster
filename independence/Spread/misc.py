from FunctionFunction import *

miscColour = ShipContainer['miscColour']

class MISC(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @bot.command(pass_context=True)
    async def 엔데버(self, ctx):
        await ctx.send(embed=shipFunction(22, 'MISC', miscColour))

    @bot.command(pass_context=True)
    async def 프리랜서(self, ctx, *free):
        free = list(free)
        free = "".join(free)
        if free == "듀오":
            await ctx.send(embed=shipFunction(12, 'MISC', miscColour))
        elif free == "맥스":
            await ctx.send(embed=shipFunction(14, 'MISC', miscColour))
        elif free == "미스":
            await ctx.send(embed=shipFunction(13, 'MISC', miscColour))
        elif free == "dur":
            await ctx.send(embed=shipFunction(12, 'MISC', miscColour))
        elif free == "max":
            await ctx.send(embed=shipFunction(14, 'MISC', miscColour))
        elif free == "mis":
            await ctx.send(embed=shipFunction(13, 'MISC', miscColour))
        elif free == "DUR":
            await ctx.send(embed=shipFunction(12, 'MISC', miscColour))
        elif free == "MAX":
            await ctx.send(embed=shipFunction(14, 'MISC', miscColour))
        elif free == "MIS":
            await ctx.send(embed=shipFunction(13, 'MISC', miscColour))
        else:
            await ctx.send(embed=shipFunction(11, 'MISC', miscColour))

    @bot.command(pass_context=True)
    async def 프리랜서듀오(self, ctx):
        await ctx.send(embed=shipFunction(12, 'MISC', miscColour))

    @bot.command(pass_context=True)
    async def 프리랜서dur(self, ctx):
        await ctx.send(embed=shipFunction(12, 'MISC', miscColour))

    @bot.command(pass_context=True)
    async def 프리랜서맥스(self, ctx):
        await ctx.send(embed=shipFunction(14, 'MISC', miscColour))

    @bot.command(pass_context=True)
    async def 프리랜서max(self, ctx):
        await ctx.send(embed=shipFunction(14, 'MISC', miscColour))

    @bot.command(pass_context=True)
    async def 프리랜서미스(self, ctx):
        await ctx.send(embed=shipFunction(13, 'MISC', miscColour))

    @bot.command(pass_context=True)
    async def 프리랜서mis(self, ctx):
        await ctx.send(embed=shipFunction(13, 'MISC', miscColour))

    @bot.command(pass_context=True)
    async def 헐(self, ctx, *hull):
        hull = list(hull)
        hull = "".join(hull)
        if hull == "a":
            await ctx.send(embed=shipFunction(17, 'MISC', miscColour))
        elif hull == "b":
            await ctx.send(embed=shipFunction(18, 'MISC', miscColour))
        elif hull == "c":
            await ctx.send(embed=shipFunction(19, 'MISC', miscColour))
        elif hull == "d":
            await ctx.send(embed=shipFunction(20, 'MISC', miscColour))
        elif hull == "e":
            await ctx.send(embed=shipFunction(21, 'MISC', miscColour))
        elif hull == "A":
            await ctx.send(embed=shipFunction(17, 'MISC', miscColour))
        elif hull == "B":
            await ctx.send(embed=shipFunction(18, 'MISC', miscColour))
        elif hull == "c":
            await ctx.send(embed=shipFunction(19, 'MISC', miscColour))
        elif hull == "D":
            await ctx.send(embed=shipFunction(20, 'MISC', miscColour))
        elif hull == "E":
            await ctx.send(embed=shipFunction(21, 'MISC', miscColour))
        else:
            await ctx.send(embed=serisFunction(23, 'MISC', miscColour))

    @bot.command(pass_context=True)
    async def 헐a(self, ctx):
        await ctx.send(embed=shipFunction(17, 'MISC', miscColour))

    @bot.command(pass_context=True)
    async def 헐b(self, ctx):
        await ctx.send(embed=shipFunction(18, 'MISC', miscColour))

    @bot.command(pass_context=True)
    async def 헐c(self, ctx):
        await ctx.send(embed=shipFunction(19, 'MISC', miscColour))

    @bot.command(pass_context=True)
    async def 헐d(self, ctx):
        await ctx.send(embed=shipFunction(20, 'MISC', miscColour))

    @bot.command(pass_context=True)
    async def 헐e(self, ctx):
        await ctx.send(embed=shipFunction(21, 'MISC', miscColour))

    @bot.command(pass_context=True)
    async def 프로스펙터(self, ctx):
        await ctx.send(embed=shipFunction(10, 'MISC', miscColour))

    @bot.command(pass_context=True)
    async def 레이저(self, ctx, *razor):
        if razor == "ex":
            await ctx.send(embed=shipFunction(4, 'MISC', miscColour))
        elif razor == "lx":
            await ctx.send(embed=shipFunction(5, 'MISC', miscColour))
        elif razor == "EX":
            await ctx.send(embed=shipFunction(4, 'MISC', miscColour))
        elif razor == "LX":
            await ctx.send(embed=shipFunction(5, 'MISC', miscColour))
        else:
            await ctx.send(embed=shipFunction(3, 'MISC', miscColour))

    @bot.command(pass_context=True)
    async def 레이저ex(self, ctx):
        await ctx.send(embed=shipFunction(4, 'MISC', miscColour))

    @bot.command(pass_context=True)
    async def 레이저lx(self, ctx):
        await ctx.send(embed=shipFunction(5, 'MISC', miscColour))

    @bot.command(pass_context=True)
    async def 릴라이언트(self, ctx, *rela):
        rela = list(rela)
        rela = "".join(rela)
        if rela == "코레":
            await ctx.send(embed=shipFunction(6, 'MISC', miscColour))
        elif rela == "마코":
            await ctx.send(embed=shipFunction(7, 'MISC', miscColour))
        elif rela == "센":
            await ctx.send(embed=shipFunction(8, 'MISC', miscColour))
        elif rela == "타나":
            await ctx.send(embed=shipFunction(9, 'MISC', miscColour))
        else:
            await ctx.send(embed=serisFunction(24, 'MISC', miscColour))

    @bot.command(pass_context=True)
    async def 릴라이언트코레(self, ctx):
        await ctx.send(embed=shipFunction(6, 'MISC', miscColour))

    @bot.command(pass_context=True)
    async def 릴라이언트마코(self, ctx):
        await ctx.send(embed=shipFunction(7, 'MISC', miscColour))

    @bot.command(pass_context=True)
    async def 릴라이언트센(self, ctx):
        await ctx.send(embed=shipFunction(8, 'MISC', miscColour))

    @bot.command(pass_context=True)
    async def 릴라이언트타나(self, ctx):
        await ctx.send(embed=shipFunction(9, 'MISC', miscColour))

    @bot.command(pass_context=True)
    async def 스타페어러(self, ctx, *farer):
        farer = list(farer)
        farer = "".join(farer)
        if farer == "제미니":
            await ctx.send(embed=shipFunction(16, 'MISC', miscColour))
        else:
            await ctx.send(embed=shipFunction(15, 'MISC', miscColour))

    @bot.command(pass_context=True)
    async def 스타페어러제미니(self, ctx, *farer):
        await ctx.send(embed=shipFunction(16, 'MISC', miscColour))

    @bot.command(pass_context=True)
    async def 제미니(self, ctx):
        await ctx.send(embed=shipFunction(16, 'MISC', miscColour))

    @bot.command(pass_context=True)
    async def 오디세이(self, ctx):
        await ctx.send(embed=shipFunction(25, 'MISC', miscColour))

    @bot.command(pass_context=True)
    async def 오딧세이(self, ctx):
        await ctx.send(embed=shipFunction(25, 'MISC', miscColour))

    @bot.command(pass_context=True)
    async def 익스펜스(self, ctx):
        await ctx.send(embed=shipFunction(26, 'MISC', miscColour))

def setup(bot):
    bot.add_cog(MISC(bot))