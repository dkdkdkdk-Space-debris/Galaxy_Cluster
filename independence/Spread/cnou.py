from FunctionFunction import *

cnouColour = ShipContainer['cnouColour']

class CNOU(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.command(pass_context=True)
    async def 파이오니어(self, ctx):
        await ctx.send(embed=shipFunction(3, 'CNOU', cnouColour))

    @bot.command(pass_context=True)
    async def 머스탱(self, ctx, *mustang):
        mustang = list(mustang)
        mustang = "".join(mustang)
        if mustang == "알파":
            await ctx.send(embed=shipFunction(4, 'CNOU', cnouColour))
        elif mustang == "베타":
            await ctx.send(embed=shipFunction(5, 'CNOU', cnouColour))
        elif mustang == "감마":
            await ctx.send(embed=shipFunction(6, 'CNOU', cnouColour))
        elif mustang == "델타":
            await ctx.send(embed=shipFunction(7, 'CNOU', cnouColour))
        elif mustang == "오메가":
            await ctx.send(embed=shipFunction(8, 'CNOU', cnouColour))
        else:
            await ctx.send(embed=serisFunction(17, 'CNOU', cnouColour))

    @bot.command(pass_context=True)
    async def 머스탱알파(self, ctx):
        await ctx.send(embed=shipFunction(4, 'CNOU', cnouColour))

    @bot.command(pass_context=True)
    async def 알파(self, ctx):
        await ctx.send(embed=shipFunction(4, 'CNOU', cnouColour))

    @bot.command(pass_context=True)
    async def 머스탱베타(ctx):
        await ctx.send(embed=shipFunction(5, 'CNOU', cnouColour))

    @bot.command(pass_context=True)
    async def 베타(self, ctx):
        await ctx.send(embed=shipFunction(5, 'CNOU', cnouColour))

    @bot.command(pass_context=True)
    async def 머스탱델타(self, ctx):
        await ctx.send(embed=shipFunction(6, 'CNOU', cnouColour))

    @bot.command(pass_context=True)
    async def 델타(self, ctx):
        await ctx.send(embed=shipFunction(6, 'CNOU', cnouColour))

    @bot.command(pass_context=True)
    async def 머스탱감마(self, ctx):
        await ctx.send(embed=shipFunction(7, 'CNOU', cnouColour))

    @bot.command(pass_context=True)
    async def 감마(self, ctx):
        await ctx.send(embed=shipFunction(7, 'CNOU', cnouColour))

    @bot.command(pass_context=True)
    async def 머스탱오메가(self, ctx):
        await ctx.send(embed=shipFunction(8, 'CNOU', cnouColour))

    @bot.command(pass_context=True)
    async def 오메가(self, ctx):
        await ctx.send(embed=shipFunction(8, 'CNOU', cnouColour))

    @bot.command(pass_context=True)
    async def 노마드(self, ctx):
        await ctx.send(embed=shipFunction(9, 'CNOU', cnouColour))

    @bot.command(pass_context=True)
    async def 노메드(self, ctx):
        await ctx.send(embed=shipFunction(9, 'CNOU', cnouColour))


def setup(bot):
    bot.add_cog(CNOU(bot))