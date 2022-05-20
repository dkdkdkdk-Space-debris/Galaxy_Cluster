from FunctionFunction import *

crusaderColour = ShipContainer['crusaderColour']

class CRUSADER(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.command(pass_context=True)
    async def 머큐리스타러너(self, ctx):
        await ctx.send(embed=shipFunction(7, 'CRUSADER', crusaderColour))

    @bot.command(pass_context=True)
    async def 머큐리(self, ctx, *mercury):
        await ctx.send(embed=shipFunction(7, 'CRUSADER', crusaderColour))

    @bot.command(pass_context=True)
    async def 아레스(self, ctx, *ares):
        ares = list(ares)
        ares = "".join(ares)
        if ares == "인페르노":
            await ctx.send(embed=shipFunction(8, 'CRUSADER', crusaderColour))
        elif ares == "이온":
            await ctx.send(embed=shipFunction(9, 'CRUSADER', crusaderColour))
        else:
            await ctx.send(embed=serisFunction(11, 'CRUSADER', crusaderColour))

    @bot.command(pass_context=True)
    async def 아레스인페르노(self, ctx):
        await ctx.send(embed=shipFunction(8, 'CRUSADER', crusaderColour))

    @bot.command(pass_context=True)
    async def 인페르노(self, ctx):
        await ctx.send(embed=shipFunction(8, 'CRUSADER', crusaderColour))

    @bot.command(pass_context=True)
    async def 아레스이온(self, ctx):
        await ctx.send(embed=shipFunction(9, 'CRUSADER', crusaderColour))

    @bot.command(pass_context=True)
    async def 이온(self, ctx):
        await ctx.send(embed=shipFunction(9, 'CRUSADER', crusaderColour))

    @bot.command(pass_context=True)
    async def 허큘리스(self, ctx, *hercul):
        hercul = list(hercul)
        hercul = "".join(hercul)
        if hercul == "a2":
            await ctx.send(embed=shipFunction(5, 'CRUSADER', crusaderColour))
        elif hercul == "m2":
            await ctx.send(embed=shipFunction(4, 'CRUSADER', crusaderColour))
        elif hercul == "c2":
            await ctx.send(embed=shipFunction(3, 'CRUSADER', crusaderColour))
        elif hercul == "A2":
            await ctx.send(embed=shipFunction(5, 'CRUSADER', crusaderColour))
        elif hercul == "M2":
            await ctx.send(embed=shipFunction(4, 'CRUSADER', crusaderColour))
        elif hercul == "C2":
            await ctx.send(embed=shipFunction(3, 'CRUSADER', crusaderColour))
        else:
            await ctx.send(embed=shipFunction(10, 'CRUSADER', crusaderColour))

    @bot.command(pass_context=True)
    async def 허큘리스a2(self, ctx):
        await ctx.send(embed=shipFunction(5, 'CRUSADER', crusaderColour))

    @bot.command(pass_context=True)
    async def a2(self, ctx):
        await ctx.send(embed=shipFunction(5, 'CRUSADER', crusaderColour))

    @bot.command(pass_context=True)
    async def m2(self, ctx):
        await ctx.send(embed=shipFunction(4, 'CRUSADER', crusaderColour))

    @bot.command(pass_context=True)
    async def 허큘리스m2(self, ctx):
        await ctx.send(embed=shipFunction(4, 'CRUSADER', crusaderColour))

    @bot.command(pass_context=True)
    async def c2(self, ctx):
        await ctx.send(embed=shipFunction(3, 'CRUSADER', crusaderColour))

    @bot.command(pass_context=True)
    async def 허큘리스c2(self, ctx):
        await ctx.send(embed=shipFunction(3, 'CRUSADER', crusaderColour))

    @bot.command(pass_context=True)
    async def 제네시스(self, ctx):
        await ctx.send(embed=shipFunction(6, 'CRUSADER', crusaderColour))

    @bot.command(pass_context=True)
    async def 스타라이너(self, ctx):
        await ctx.send(embed=shipFunction(6, 'CRUSADER', crusaderColour))


def setup(bot):
    bot.add_cog(CRUSADER(bot))