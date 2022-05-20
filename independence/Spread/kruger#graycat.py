
from FunctionFunction import *

krugerColour = ShipContainer['krugerColour']
greycatColour = ShipContainer['greycatColour']


class KRUGER(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.command(pass_context=True)
    async def 멀린(self, ctx):
        await ctx.send(embed=shipFunction(3, 'KRUGER/GRAYCAT', krugerColour))

    @bot.command(pass_context=True)
    async def 아르키메데스(self, ctx):
        await ctx.send(embed=shipFunction(4, 'KRUGER/GRAYCAT', krugerColour))

    # 그레이캣

    @bot.command(pass_context=True)
    async def ptv(self, ctx):
        await ctx.send(embed=shipFunction(7, 'KRUGER/GRAYCAT', greycatColour))

    @bot.command(pass_context=True)
    async def 버기(self, ctx):
        await ctx.send(embed=shipFunction(7, 'KRUGER/GRAYCAT', greycatColour))

    @bot.command(pass_context=True)
    async def roc(self, ctx, *ro):
        ro = list(ro)
        ro = "".join(ro)
        if ro == 'ds':
            await ctx.send(embed=shipFunction(6, 'KRUGER/GRAYCAT', greycatColour))
        elif ro == 'DS':
            await ctx.send(embed=shipFunction(6, 'KRUGER/GRAYCAT', greycatColour))
        else:
            await ctx.send(embed=shipFunction(5, 'KRUGER/GRAYCAT', greycatColour))


def setup(bot):
    bot.add_cog(KRUGER(bot))