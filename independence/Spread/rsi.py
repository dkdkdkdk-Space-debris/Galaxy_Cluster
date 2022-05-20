from FunctionFunction import *

rsiColour = ShipContainer['rsiColour']

class RSI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.command(pass_context=True)
    async def 아폴로(self, ctx, *apollo):
        apollo = "".join(apollo)
        if apollo == '트리아지':
            await ctx.send(embed=shipFunction(6, 'RSI', rsiColour))
        elif apollo == '메디백':
            await ctx.send(embed=shipFunction(5, 'RSI', rsiColour))
        else:
            await ctx.send(embed=serisFunction(22,'RSI', rsiColour))

    @bot.command(pass_context=True)
    async def 아폴로트리아지(self, ctx):
        await ctx.send(embed=shipFunction(6, 'RSI', rsiColour))

    @bot.command(pass_context=True)
    async def 트리아지(self, ctx):
        await ctx.send(embed=shipFunction(6, 'RSI', rsiColour))

    @bot.command(pass_context=True)
    async def 아폴로메디백(self, ctx):
        await ctx.send(embed=shipFunction(6, 'RSI', rsiColour))

    @bot.command(pass_context=True)
    async def 메디백(self, ctx):
        await ctx.send(embed=shipFunction(5, 'RSI', rsiColour))

    @bot.command(pass_context=True)
    async def 오로라(self, ctx, *aurora):
        aurora = "".join(aurora)
        if aurora == 'es':
            await ctx.send(embed=shipFunction(8, 'RSI', rsiColour))
        elif aurora == 'lx':
            await ctx.send(embed=shipFunction(10, 'RSI', rsiColour))
        elif aurora == 'mr':
            await ctx.send(embed=shipFunction(11, 'RSI', rsiColour))
        elif aurora == 'cl':
            await ctx.send(embed=shipFunction(7, 'RSI', rsiColour))
        elif aurora == 'ln':
            await ctx.send(embed=shipFunction(9, 'RSI', rsiColour))
        elif aurora == 'ES':
            await ctx.send(embed=shipFunction(8, 'RSI', rsiColour))
        elif aurora == 'LX':
            await ctx.send(embed=shipFunction(10, 'RSI', rsiColour))
        elif aurora == 'MR':
            await ctx.send(embed=shipFunction(11, 'RSI', rsiColour))
        elif aurora == 'CL':
            await ctx.send(embed=shipFunction(7, 'RSI', rsiColour))
        elif aurora == 'LN':
            await ctx.send(embed=shipFunction(9, 'RSI', rsiColour))
        else:
            await ctx.send(embed=serisFunction(23,'RSI', rsiColour))

    @bot.command(pass_context=True)
    async def 오로롱(self, ctx):
        await ctx.send(embed=serisFunction(23,'RSI', rsiColour))


    @bot.command(pass_context=True)
    async def 오로라es(self, ctx):
        await ctx.send(embed=shipFunction(8, 'RSI', rsiColour))

    @bot.command(pass_context=True)
    async def 오로라lx(self, ctx):
        await ctx.send(embed=shipFunction(10, 'RSI', rsiColour))

    @bot.command(pass_context=True)
    async def 오로라mr(self, ctx):
        await ctx.send(embed=shipFunction(11, 'RSI', rsiColour))

    @commands.command(pass_context=True)
    async def 오로라cl(self, ctx):
        await ctx.send(embed=shipFunction(7, 'RSI', rsiColour))

    @bot.command(pass_context=True)
    async def 오로라ln(self, ctx):
        await ctx.send(embed=shipFunction(9, 'RSI', rsiColour))

    @bot.command(pass_context=True)
    async def 맨티스(self, ctx):
        await ctx.send(embed=shipFunction(3, 'RSI', rsiColour))

    @bot.command(pass_context=True)
    async def 뱅갈(self, ctx):
        await ctx.send(embed=shipFunction(4, 'RSI', rsiColour))

    @bot.command(pass_context=True)
    async def 오리온(self, ctx):
        await ctx.send(embed=shipFunction(12, 'RSI', rsiColour))

    @bot.command(pass_context=True)
    async def 폴라리스(self, ctx):
        await ctx.send(embed=shipFunction(18, 'RSI', rsiColour))

    @bot.command(pass_context=True)
    async def 컨스틸레이션(self, ctx, *coni):
        coni = "".join(coni)
        if coni == '안드로메다':
            await ctx.send(embed=shipFunction(14, 'RSI', rsiColour))
        elif coni == '타우러스':
            await ctx.send(embed=shipFunction(15, 'RSI', rsiColour))
        elif coni == '아퀼라':
            await ctx.send(embed=shipFunction(13, 'RSI', rsiColour))
        elif coni == '피닉스':
            await ctx.send(embed=shipFunction(16, 'RSI', rsiColour))
        else:
            await ctx.send(embed=serisFunction(24,'RSI', rsiColour))
    @bot.command(pass_context=True)
    async def 별자리(self, ctx):
        await ctx.send(embed=serisFunction(24,'RSI', rsiColour))
    @bot.command(pass_context=True)
    async def 코니(self, ctx):
        await ctx.send(embed=serisFunction(24,'RSI', rsiColour))

    @bot.command(pass_context=True)
    async def 컨스틸레이션안드로메다(self, ctx):
        await ctx.send(embed=shipFunction(14, 'RSI', rsiColour))

    @bot.command(pass_context=True)
    async def 컨스틸레이션타우러스(self, ctx):
        await ctx.send(embed=shipFunction(15, 'RSI', rsiColour))

    @bot.command(pass_context=True)
    async def 컨스틸레이션아퀼라(self, ctx):
        await ctx.send(embed=shipFunction(13, 'RSI', rsiColour))

    @bot.command(pass_context=True)
    async def 컨스틸레이션피닉스(self, ctx):
        await ctx.send(embed=shipFunction(16, 'RSI', rsiColour))

    @bot.command(pass_context=True)
    async def 안드로메다(self, ctx):
        await ctx.send(embed=shipFunction(14, 'RSI', rsiColour))

    @bot.command(pass_context=True)
    async def 타우러스(self, ctx):
        await ctx.send(embed=shipFunction(15, 'RSI', rsiColour))

    @bot.command(pass_context=True)
    async def 아퀼라(self, ctx):
        await ctx.send(embed=shipFunction(13, 'RSI', rsiColour))

    @bot.command(pass_context=True)
    async def 피닉스(self, ctx):
        await ctx.send(embed=shipFunction(16, 'RSI', rsiColour))

    @bot.command(pass_context=True)
    async def 얼사로버(self, ctx):
        await ctx.send(embed=shipFunction(19, 'RSI', rsiColour))

    @bot.command(pass_context=True)
    async def 얼사(self, ctx, *ursa):
        ursa = "".join(ursa)
        if ursa == '로버':
            await ctx.send(embed=shipFunction(19, 'RSI', rsiColour))
        else:
            await ctx.send(embed=shipFunction(19, 'RSI', rsiColour))

    @bot.command(pass_context=True)
    async def 우르사로버(self, ctx):
        await ctx.send(embed=shipFunction(19, 'RSI', rsiColour))

    @bot.command(pass_context=True)
    async def 로버(self, ctx):
        await ctx.send(embed=shipFunction(19, 'RSI', rsiColour))

    @bot.command(pass_context=True)
    async def 포투나(self, ctx):
        await ctx.send(embed=shipFunction(21, 'RSI', rsiColour))

    @bot.command(pass_context=True)
    async def 우르사(self, ctx, *ursa):
        ursa = "".join(ursa)
        if ursa == '로버':
            await ctx.send(embed=shipFunction(19, 'RSI', rsiColour))
        else:
            await ctx.send(embed=shipFunction(19, 'RSI', rsiColour))

    @bot.command(pass_context=True)
    async def ursa(self, ctx):
        await ctx.send(embed=shipFunction(19, 'RSI', rsiColour))

    @bot.command(pass_context=True)
    async def 페르세우스(self, ctx):
        await ctx.send(embed=shipFunction(17, 'RSI', rsiColour))

    @bot.command(pass_context=True)
    async def 스콜피우스(self, ctx):
        await ctx.send(embed=shipFunction(20, 'RSI', rsiColour))

    @bot.command(pass_context=True)
    async def 스콜피어스(self, ctx):
        await ctx.send(embed=shipFunction(20, 'RSI', rsiColour))

def setup(bot):
    bot.add_cog(RSI(bot))