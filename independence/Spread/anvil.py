from FunctionFunction import *

anvilColour = ShipContainer['anvilColour']

class ANVIL(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.command(pass_context=True)
    async def 호넷(self, ctx, *hornet):
        hornet = list(hornet)
        hornet = "".join(hornet)
        if hornet == '고스트':
            await ctx.send(embed=shipFunction(17, 'ANVIL', anvilColour))
        elif hornet == '트랙커':
            await ctx.send(embed=shipFunction(16, 'ANVIL', anvilColour))
        elif hornet == '와일드파이어':
            await ctx.send(embed=shipFunction(22, 'ANVIL', anvilColour))
        elif hornet == '하트시커':
            await ctx.send(embed=shipFunction(23, 'ANVIL', anvilColour))
        else:
            await ctx.send(embed=shipFunction(14, 'ANVIL', anvilColour))

    @bot.command(pass_context=True)
    async def 호넷고스트(self, ctx):
        await ctx.send(embed=shipFunction(17, 'ANVIL', anvilColour))

    @bot.command(pass_context=True)
    async def 호넷트랙커(self, ctx):
        await ctx.send(embed=shipFunction(16, 'ANVIL', anvilColour))

    @bot.command(pass_context=True)
    async def 호넷트래커(self, ctx):
        await ctx.send(embed=shipFunction(16, 'ANVIL', anvilColour))

    @bot.command(pass_context=True)
    async def 호넷트레커(self, ctx):
        await ctx.send(embed=shipFunction(16, 'ANVIL', anvilColour))

    @bot.command(pass_context=True)
    async def 호넷트렉커(self, ctx):
        await ctx.send(embed=shipFunction(16, 'ANVIL', anvilColour))

    @bot.command(pass_context=True)
    async def 슈퍼호넷(self, ctx):
        await ctx.send(embed=shipFunction(15, 'ANVIL', anvilColour))

    @bot.command(pass_context=True)
    async def 호넷와일드파이어(self, ctx):
        await ctx.send(embed=shipFunction(22, 'ANVIL', anvilColour))

    @bot.command(pass_context=True)
    async def 호넷하트시커(self, ctx):
        await ctx.send(embed=shipFunction(23, 'ANVIL', anvilColour))


    @bot.command(pass_context=True)
    async def 슈퍼(self, ctx, *hornet):
        hornet = list(hornet)
        hornet = "".join(hornet)
        if hornet == '호넷':
            await ctx.send(embed=shipFunction(15, 'ANVIL', anvilColour))

    @bot.command(pass_context=True)
    async def 군용호넷(self, ctx):
        await ctx.send(embed=shipFunction(13, 'ANVIL', anvilColour))

    @bot.command(pass_context=True)
    async def f7a(self, ctx, *hornet):
        hornet = list(hornet)
        hornet = "".join(hornet)
        if hornet == '호넷':
            await ctx.send(embed=shipFunction(13, 'ANVIL', anvilColour))
        else:
            await ctx.send(embed=shipFunction(13, 'ANVIL', anvilColour))

    @bot.command(pass_context=True)
    async def 글래디에이터(self, ctx):
        await ctx.send(embed=shipFunction(3, 'ANVIL', anvilColour))

    @bot.command(pass_context=True)
    async def 글레디에이터(self, ctx):
        await ctx.send(embed=shipFunction(3, 'ANVIL', anvilColour))

    @bot.command(pass_context=True)
    async def 글래디(self, ctx):
        await ctx.send(embed=shipFunction(3, 'ANVIL', anvilColour))

    @bot.command(pass_context=True)
    async def 글레디(self, ctx):
        await ctx.send(embed=shipFunction(3, 'ANVIL', anvilColour))

    @bot.command(pass_context=True)
    async def 캐럭(self, ctx):
        await ctx.send(embed=shipFunction(6, 'ANVIL', anvilColour))

    @bot.command(pass_context=True)
    async def 크루시블(self, ctx):
        await ctx.send(embed=shipFunction(7, 'ANVIL', anvilColour))

    @bot.command(pass_context=True)
    async def 테라핀(self, ctx):
        await ctx.send(embed=shipFunction(8, 'ANVIL', anvilColour))

    @bot.command(pass_context=True)
    async def 호크(self, ctx):
        await ctx.send(embed=shipFunction(12, 'ANVIL', anvilColour))

    @bot.command(pass_context=True)
    async def 발키리(self, ctx):
        await ctx.send(embed=shipFunction(4, 'ANVIL', anvilColour))

    @bot.command(pass_context=True)
    async def 허리케인(self, ctx):
        await ctx.send(embed=shipFunction(11, 'ANVIL', anvilColour))

    @bot.command(pass_context=True)
    async def 파이시스(self, ctx, *pisis):
        pisis = list(pisis)
        pisis = "".join(pisis)
        if pisis == '익스페디션':
            await ctx.send(embed=shipFunction(10, 'ANVIL', anvilColour))
        else:
            await ctx.send(embed=shipFunction(9, 'ANVIL', anvilColour))

    @bot.command(pass_context=True)
    async def 파이시스익스페디션(self, ctx):
        await ctx.send(embed=shipFunction(10, 'ANVIL', anvilColour))

    @bot.command(pass_context=True)
    async def 라이트닝(self, ctx):
        await ctx.send(embed=shipFunction(18, 'ANVIL', anvilColour))

    @bot.command(pass_context=True)
    async def 발리스타(self, ctx):
        await ctx.send(embed=shipFunction(19, 'ANVIL', anvilColour))

    @bot.command(pass_context=True)
    async def 애로우(self, ctx):
        await ctx.send(embed=shipFunction(5, 'ANVIL', anvilColour))

    @bot.command(pass_context=True)
    async def 에로우(self, ctx):
        await ctx.send(embed=shipFunction(5, 'ANVIL', anvilColour))

    @bot.command(pass_context=True)
    async def 리버레이터(self, ctx):
        await ctx.send(embed=shipFunction(20, 'ANVIL', anvilColour))

    @bot.command(pass_context=True)
    async def 스파르탄(self, ctx):
        await ctx.send(embed=shipFunction(21, 'ANVIL', anvilColour))

    @bot.command(pass_context=True)
    async def 스파르타(self, ctx):
        await ctx.send(embed=shipFunction(21, 'ANVIL', anvilColour))

    @bot.command(pass_context=True)
    async def 디스이즈(self, ctx):
        await ctx.send(embed=shipFunction(21, 'ANVIL', anvilColour))

def setup(bot):
    bot.add_cog(ANVIL(bot))