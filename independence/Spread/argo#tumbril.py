from FunctionFunction import *

argoColour = ShipContainer['argoColour']
tumbrilColour = ShipContainer['tumbrilColour']

class ARGO(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @bot.command(pass_context=True)
    async def 아르고(self, ctx, *argo):
        argo = list(argo)
        argo = "".join(argo)
        if argo =='몰':
            await ctx.send(embed=shipFunction(3, 'ARGO', argoColour))
        elif argo == '퍼스널':
            await ctx.send(embed=shipFunction(5, 'ARGO', argoColour))
        elif argo == '카고':
            await ctx.send(embed=shipFunction(4, 'ARGO', argoColour))

    @bot.command(pass_context=True)
    async def mpuv(self, ctx, *argo):
        argo = list(argo)
        argo = "".join(argo)
        if argo == '퍼스널':
            await ctx.send(embed=shipFunction(5, 'ARGO', argoColour))
        elif argo == '카고':
            await ctx.send(embed=shipFunction(4, 'ARGO', argoColour))

    @bot.command(pass_context=True)
    async def 아르고몰(self, ctx):
        await ctx.send(embed=shipFunction(3, 'ARGO', argoColour))

    @bot.command(pass_context=True)
    async def 몰(self, ctx):
        await ctx.send(embed=shipFunction(3, 'ARGO', argoColour))

    @bot.command(pass_context=True)
    async def 아르고퍼스널(self, ctx):
        await ctx.send(embed=shipFunction(5, 'ARGO', argoColour))

    @bot.command(pass_context=True)
    async def 퍼스널(self, ctx):
        await ctx.send(embed=shipFunction(5, 'ARGO', argoColour))

    @bot.command(pass_context=True)
    async def mpuv퍼스널(self, ctx):
        await ctx.send(embed=shipFunction(5, 'ARGO', argoColour))

    @bot.command(pass_context=True)
    async def 아르고카고(self, ctx):
        await ctx.send(embed=shipFunction(4, 'ARGO', argoColour))

    @bot.command(pass_context=True)
    async def 카고(self, ctx):
        await ctx.send(embed=shipFunction(4, 'ARGO', argoColour))

    @bot.command(pass_context=True)
    async def mpuv카고(self, ctx):
        await ctx.send(embed=shipFunction(4, 'ARGO', argoColour))

    @bot.command(pass_context=True)
    async def srv(self, ctx):
        await ctx.send(embed=shipFunction(6, 'ARGO', argoColour))

    @bot.command(pass_context=True)
    async def 레프트(self, ctx):
        await ctx.send(embed=shipFunction(7, 'ARGO', argoColour))

    @bot.command(pass_context=True)
    async def 래프트(self, ctx):
        await ctx.send(embed=shipFunction(7, 'ARGO', argoColour))

    @bot.command(pass_context=True)
    async def raft(self, ctx):
        await ctx.send(embed=shipFunction(7, 'ARGO', argoColour))

#텀브릴
    @bot.command(pass_context=True)
    async def 사이클론(self, ctx, *cyclone):
        cyclone = list(cyclone)
        cyclone = "".join(cyclone)
        if cyclone == 'tr':
            await ctx.send(embed=shipFunction(4, 'TUMBRIL', tumbrilColour))
        elif cyclone == 'rn':
            await ctx.send(embed=shipFunction(5, 'TUMBRIL', tumbrilColour))
        elif cyclone == 'rc':
            await ctx.send(embed=shipFunction(6, 'TUMBRIL', tumbrilColour))
        elif cyclone == 'aa':
            await ctx.send(embed=shipFunction(7, 'TUMBRIL', tumbrilColour))
        else:
            await ctx.send(embed=shipFunction(3, 'TUMBRIL', tumbrilColour))
    @bot.command(pass_context=True)
    async def 싸이클론(self, ctx, *cyclone):
        cyclone = list(cyclone)
        cyclone = "".join(cyclone)
        if cyclone == 'tr':
            await ctx.send(embed=shipFunction(4, 'TUMBRIL', tumbrilColour))
        elif cyclone == 'rn':
            await ctx.send(embed=shipFunction(5, 'TUMBRIL', tumbrilColour))
        elif cyclone == 'rc':
            await ctx.send(embed=shipFunction(6, 'TUMBRIL', tumbrilColour))
        elif cyclone == 'aa':
            await ctx.send(embed=shipFunction(7, 'TUMBRIL', tumbrilColour))
        else:
            await ctx.send(embed=shipFunction(3, 'TUMBRIL', tumbrilColour))

    @bot.command(pass_context=True)
    async def 사이클론tr(self, ctx):
        await ctx.send(embed=shipFunction(4, 'TUMBRIL', tumbrilColour))

    @bot.command(pass_context=True)
    async def 사이클론rn(self, ctx):
        await ctx.send(embed=shipFunction(5, 'TUMBRIL', tumbrilColour))

    @bot.command(pass_context=True)
    async def 사이클론rc(self, ctx):
        await ctx.send(embed=shipFunction(6, 'TUMBRIL', tumbrilColour))

    @bot.command(pass_context=True)
    async def 사이클론aa(self, ctx):
        await ctx.send(embed=shipFunction(8, 'TUMBRIL', tumbrilColour))

    @bot.command(pass_context=True)
    async def 사이클론mt(self, ctx):
        await ctx.send(embed=shipFunction(7, 'TUMBRIL', tumbrilColour))

    @bot.command(pass_context=True)
    async def 싸이클론tr(self, ctx):
        await ctx.send(embed=shipFunction(4, 'TUMBRIL', tumbrilColour))

    @bot.command(pass_context=True)
    async def 싸이클론rn(self, ctx):
        await ctx.send(embed=shipFunction(5, 'TUMBRIL', tumbrilColour))

    @bot.command(pass_context=True)
    async def 싸이클론rc(self, ctx):
        await ctx.send(embed=shipFunction(6, 'TUMBRIL', tumbrilColour))

    @bot.command(pass_context=True)
    async def 싸이클론aa(self, ctx):
        await ctx.send(embed=shipFunction(7, 'TUMBRIL', tumbrilColour))

    @bot.command(pass_context=True)
    async def 싸이클론mt(self, ctx):
        await ctx.send(embed=shipFunction(8, 'TUMBRIL', tumbrilColour))

    @bot.command(pass_context=True)
    async def 레인저(self, ctx, *ranger):
        cyclone = list(ranger)
        cyclone = "".join(ranger)
        if cyclone == 'tr':
            await ctx.send(embed=shipFunction(9, 'TUMBRIL', tumbrilColour))
        elif cyclone == 'rc':
            await ctx.send(embed=shipFunction(10, 'TUMBRIL', tumbrilColour))
        elif cyclone == 'cv':
            await ctx.send(embed=shipFunction(11, 'TUMBRIL', tumbrilColour))
        else:
            await ctx.send(embed=serisFunction(15, 'TUMBRIL', tumbrilColour))

    @bot.command(pass_context=True)
    async def 레인저tr(self, ctx):
        await ctx.send(embed=shipFunction(9, 'TUMBRIL', tumbrilColour))

    @bot.command(pass_context=True)
    async def 레인저rc(self, ctx):
        await ctx.send(embed=shipFunction(10, 'TUMBRIL', tumbrilColour))

    @bot.command(pass_context=True)
    async def 레인저cv(self, ctx):
        await ctx.send(embed=shipFunction(1, 'TUMBRIL', tumbrilColour))

    @bot.command(pass_context=True)
    async def 노바(self, ctx):
        await ctx.send(embed=shipFunction(12, 'TUMBRIL', tumbrilColour))


def setup(bot):
    bot.add_cog(ARGO(bot))
