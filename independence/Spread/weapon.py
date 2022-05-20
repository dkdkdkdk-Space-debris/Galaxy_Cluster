from FunctionFunction import *




class wea(commands.Cog):

    def __init__(self,bot):
        self.bot=bot

    @bot.command(pass_context=True)
    async def 무기(self, ctx, *arg):
        arg = "".join(arg)
        if arg == "":
            await ctx.send(embed=ComIntroFunction(25, 'intro'))
        else:
            ws = ss.worksheet('weapon')
            raw = str(ws.find(arg).row)
            await ctx.send(embed=WeaponFunction(raw, 'weapon'))

    @bot.command(pass_context=True)
    async def 미사일(self, ctx, *arg):
        arg = "".join(arg)
        if arg == "":
            await ctx.send(embed=ComIntroFunction(26, 'intro'))
        elif arg == "랙":
            await ctx.send(embed=ComIntroFunction(28, 'intro'))
        else:
            ws = ss.worksheet('missile')
            raw = str(ws.find(arg).row)
            await ctx.send(embed=MissileFunction(raw, 'missile'))

    @bot.command(pass_context=True)
    async def 어뢰(self, ctx, *arg):
        arg = "".join(arg)
        if arg == "":
            await ctx.send(embed=
                           await ctx.send(embed=ComIntroFunction(27, 'intro')))
        else:
            ws = ss.worksheet('missile')
            raw = str(ws.find(arg).row)
            await ctx.send(embed=MissileFunction(raw, 'missile'))

    @bot.command(pass_context=True)
    async def 발리스틱(self, ctx, *arg):
        arg = "".join(arg)
        if arg == '캐논':
            await ctx.send(embed=ComIntroFunction(17, 'intro'))
        elif arg == '개틀링':
            await ctx.send(embed=ComIntroFunction(18, 'intro'))
        elif arg == '리피터':
            await ctx.send(embed=ComIntroFunction(19, 'intro'))
        elif arg == '스캐터건':
            await ctx.send(embed=ComIntroFunction(20, 'intro'))
        elif arg == '매스 드라이버':
            await ctx.send(embed=ComIntroFunction(22, 'intro'))
        else:
            await ctx.send(embed=ComIntroFunction(13, 'intro'))

    @bot.command(pass_context=True)
    async def 디스토션(self, ctx, *arg):
        arg = "".join(arg)
        if arg == '캐논':
            await ctx.send(embed=ComIntroFunction(17, 'intro'))
        elif arg == '리피터':
            await ctx.send(embed=ComIntroFunction(18, 'intro'))
        elif arg == '스캐터건':
            await ctx.send(embed=ComIntroFunction(20, 'intro'))
        else:
            await ctx.send(embed=ComIntroFunction(14, 'intro'))

    @bot.command(pass_context=True)
    async def 에너지(self, ctx, *arg):
        arg = "".join(arg)
        if arg == '캐논':
            await ctx.send(embed=ComIntroFunction(17, 'intro'))
        elif arg == '리피터':
            await ctx.send(embed=ComIntroFunction(19, 'intro'))
        elif arg == '뉴트론':
            await ctx.send(embed=ComIntroFunction(23, 'intro'))
        elif arg == '스캐터건':
            await ctx.send(embed=ComIntroFunction(20, 'intro'))
        elif arg == '타키온':
            await ctx.send(embed=ComIntroFunction(21, 'intro'))
        else:
            await ctx.send(embed=ComIntroFunction(15, 'intro'))

def setup(bot):
    bot.add_cog(wea(bot))