from FunctionFunction import *

originColour = ShipContainer['originColour']

class ORIGIN(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.command(name='100')
    async def _100(self, ctx):
        await ctx.send(embed=serisFunction(22, 'ORIGIN', originColour))

    @bot.command(name="100i")
    async def _100i(self, ctx):
        await ctx.send(embed=shipFunction(11, 'ORIGIN', originColour))

    @bot.command(name="125a")
    async def _125a(self, ctx):
        await ctx.send(embed=shipFunction(12, 'ORIGIN', originColour))

    @bot.command(name="135c")
    async def _135c(self, ctx):
        await ctx.send(embed=shipFunction(13, 'ORIGIN', originColour))

    @bot.command(name='300')
    async def _300(self, ctx):
        await ctx.send(embed=serisFunction(23, 'ORIGIN', originColour))

    @bot.command(name="300i")
    async def _300i(self, ctx):
        await ctx.send(embed=shipFunction(14, 'ORIGIN', originColour))

    @bot.command(name="315p")
    async def _315p(self, tx):
        await ctx.send(embed=shipFunction(15, 'ORIGIN', originColour))

    @bot.command(name="325a")
    async def _325a(self, ctx):
        await ctx.send(embed=shipFunction(16, 'ORIGIN', originColour))

    @bot.command(name="350r")
    async def _350r(self, ctx):
        await ctx.send(embed=shipFunction(17, 'ORIGIN', originColour))

    @bot.command(name="400i")
    async def _400i(self, ctx):
        await ctx.send(embed=shipFunction(20, 'ORIGIN', originColour))

    @bot.command(name="600i")
    async def _600i(self, ctx):
        await ctx.send(embed=shipFunction(18, 'ORIGIN', originColour))

    @bot.command(name="890점프")
    async def _890점프(self, ctx):
        await ctx.send(embed=shipFunction(19, 'ORIGIN', originColour))

    @bot.command(name="890jump")
    async def _890jump(self, ctx):
        await ctx.send(embed=shipFunction(19, 'ORIGIN', originColour))

    @bot.command(name="890")
    async def _890(self, ctx):
        await ctx.send(embed=shipFunction(19, 'ORIGIN', originColour))

    @bot.command(name="85x")
    async def _85x(self, ctx):
        await ctx.send(embed=shipFunction(10, 'ORIGIN', originColour))

    @bot.command(pass_context=True)
    async def m50(self, ctx):
        await ctx.send(embed=shipFunction(9, 'ORIGIN', originColour))

    @bot.command(pass_context=True)
    async def g12(self, ctx):
        await ctx.send(embed=shipFunction(6, 'ORIGIN', originColour))

    @bot.command(pass_context=True)
    async def g12a(self, ctx):
        await ctx.send(embed=shipFunction(7, 'ORIGIN', originColour))

    @bot.command(pass_context=True)
    async def g12r(self, ctx):
        await ctx.send(embed=shipFunction(8, 'ORIGIN', originColour))

    @bot.command(pass_context=True)
    async def x1(self, ctx, *x1):
        x1 = list(x1)
        x1 = "".join(x1)
        if x1 == "벨로시티":
            await ctx.send(embed=shipFunction(5, 'ORIGIN', originColour))
        elif x1 == "포스":
            await ctx.send(embed=shipFunction(4, 'ORIGIN', originColour))
        elif x1 == '베이스':
            await ctx.send(embed=shipFunction(3, 'ORIGIN', originColour))
        else:
            await ctx.send(embed=serisFunction(24, 'ORIGIN', originColour))

    @bot.command(pass_context=True)
    async def x1벨로시티(self, ctx):
        await ctx.send(embed=shipFunction(5, 'ORIGIN', originColour))

    @bot.command(pass_context=True)
    async def x1포스(self, ctx):
        await ctx.send(embed=shipFunction(4, 'ORIGIN', originColour))


def setup(bot):
    bot.add_cog(ORIGIN(bot))