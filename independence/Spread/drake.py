from FunctionFunction import *

drakeColour = ShipContainer['drakeColour']

class DRAKE(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @bot.command(pass_context=True)
    async def 버캐니어(self, ctx):
        await ctx.send(embed=shipFunction(3, 'DRAKE', drakeColour))

    @bot.command(pass_context=True)
    async def 버케니어(self, ctx):
        await ctx.send(embed=shipFunction(3, 'DRAKE', drakeColour))

    @bot.command(pass_context=True)
    async def 해럴드(self, ctx):
        await ctx.send(embed=shipFunction(4, 'DRAKE', drakeColour))

    @bot.command(pass_context=True)
    async def 헤럴드(self, ctx):
        await ctx.send(embed=shipFunction(4, 'DRAKE', drakeColour))

    @bot.command(pass_context=True)
    async def 커세어(self, ctx):
        await ctx.send(embed=shipFunction(8, 'DRAKE', drakeColour))

    @bot.command(pass_context=True)
    async def 크라켄(self, ctx, *kraken):
        kraken = list(kraken)
        kraken = "".join(kraken)
        if kraken == '프리베이터':
            await ctx.send(embed=shipFunction(6, 'DRAKE', drakeColour))
        elif kraken == '프라이버티어':
            await ctx.send(embed=shipFunction(6, 'DRAKE', drakeColour))
        else:
            await ctx.send(embed=shipFunction(7, 'DRAKE', drakeColour))

    @bot.command(pass_context=True)
    async def 크라켄프리베이터(self, ctx):
        await ctx.send(embed=shipFunction(6, 'DRAKE', drakeColour))

    @bot.command(pass_context=True)
    async def 프리베이터(self, ctx):
        await ctx.send(embed=shipFunction(6, 'DRAKE', drakeColour))

    @bot.command(pass_context=True)
    async def 크라켄프라이버티어(self, ctx):
        await ctx.send(embed=shipFunction(6, 'DRAKE', drakeColour))

    @bot.command(pass_context=True)
    async def 벌처(self, ctx):
        await ctx.send(embed=shipFunction(9, 'DRAKE', drakeColour))

    @bot.command(pass_context=True)
    async def 벌쳐(self, ctx):
        await ctx.send(embed=shipFunction(9, 'DRAKE', drakeColour))

    @bot.command(pass_context=True)
    async def 커틀라스(self, ctx, *cutl):
        cutl = list(cutl)
        cutl = "".join(cutl)
        if cutl == "레드":
            await ctx.send(embed=shipFunction(11, 'DRAKE', drakeColour))
        elif cutl == "블루":
            await ctx.send(embed=shipFunction(12, 'DRAKE', drakeColour))
        elif cutl == "블랙":
            await ctx.send(embed=shipFunction(10, 'DRAKE', drakeColour))
        elif cutl == "스틸":
            await ctx.send(embed=shipFunction(14, 'DRAKE', drakeColour))
        else:
            await ctx.send(embed=serisFunction(17, 'DRAKE', drakeColour))

    @bot.command(pass_context=True)
    async def 커틀라스레드(self, ctx):
        await ctx.send(embed=shipFunction(11, 'DRAKE', drakeColour))

    @bot.command(pass_context=True)
    async def 레드(self, ctx):
        await ctx.send(embed=shipFunction(11, 'DRAKE', drakeColour))

    @bot.command(pass_context=True)
    async def 커틀라스블랙(self, ctx):
        await ctx.send(embed=shipFunction(10, 'DRAKE', drakeColour))

    @bot.command(pass_context=True)
    async def 블랙(self, ctx):
        await ctx.send(embed=shipFunction(10, 'DRAKE', drakeColour))

    @bot.command(pass_context=True)
    async def 커틀라스블루(self, ctx):
        await ctx.send(embed=shipFunction(12, 'DRAKE', drakeColour))

    @bot.command(pass_context=True)
    async def 블루(self, ctx):
        await ctx.send(embed=shipFunction(12, 'DRAKE', drakeColour))

    @bot.command(pass_context=True)
    async def 커틀라스스틸(self, ctx):
        await ctx.send(embed=shipFunction(14, 'DRAKE', drakeColour))

    @bot.command(pass_context=True)
    async def 스틸(self, ctx):
        await ctx.send(embed=shipFunction(14, 'DRAKE', drakeColour))

    @bot.command(pass_context=True)
    async def 캐터필러(self, ctx):
        await ctx.send(embed=shipFunction(5, 'DRAKE', drakeColour))

    @bot.command(pass_context=True)
    async def 드래곤플라이(self, ctx):
        await ctx.send(embed=shipFunction(13, 'DRAKE', drakeColour))

    @bot.command(pass_context=True)
    async def 드플(self, ctx):
        await ctx.send(embed=shipFunction(13, 'DRAKE', drakeColour))


def setup(bot):
    bot.add_cog(DRAKE(bot))