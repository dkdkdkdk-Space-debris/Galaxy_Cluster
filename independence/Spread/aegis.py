from FunctionFunction import *
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

aegisColour = ShipContainer['aegisColour']

class AEGIS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name='자벨린', description= '세부함선 없음',guild_ids=[960397196145078333])
    async def _자벨린(self, ctx: SlashContext):
        embed = shipFunction(23, 'AEGIS', aegisColour)
        await ctx.send(embeds=[embed])

    @bot.command(pass_context=True)
    async def 자벨린(self, ctx):
        await ctx.send(embed=shipFunction(23, 'AEGIS', aegisColour))



    @cog_ext.cog_slash(name='이드리스',
                 description='세부함선: 이드리스 P, 이드리스 M,  이드리스 K',
                 guild_ids=[960397196145078333],
                 options=[
                     create_option(
                         name='세부함선 명',
                         description='세부함선명을 골라주세요',
                         required=True,
                         option_type=3,
                         choices=[create_choice(name='P', value = 'p'),
                                  create_choice(name='M', value = 'm'),
                                  create_choice(name='K', value = 'k'),
                                  create_choice(name=' ', value = 'none')]
                     )
                 ]
                 )
    async def _이드리스(self, ctx: SlashContext, 세부함선:str):
        if 세부함선 == 'm':
            await ctx.send(embed=shipFunction(20, 'AEGIS', aegisColour))
        elif 세부함선 == 'k':
            await ctx.send(embed=shipFunction(19, 'AEGIS', aegisColour))
        elif 세부함선 == 'K':
            await ctx.send(embed=shipFunction(19, 'AEGIS', aegisColour))
        else:
            await ctx.send(embed=shipFunction(21, 'AEGIS', aegisColour))


    @bot.command(pass_context=True)
    async def 이드리스(self, ctx, *idris):
        idris = list(idris)
        idris = "".join(idris)
        if idris == 'm':
            await ctx.send(embed=shipFunction(20, 'AEGIS', aegisColour))
        elif idris == 'M':
            await ctx.send(embed=shipFunction(20, 'AEGIS', aegisColour))
        elif idris == 'k':
            await ctx.send(embed=shipFunction(19, 'AEGIS', aegisColour))
        elif idris == 'K':
            await ctx.send(embed=shipFunction(19, 'AEGIS', aegisColour))
        else:
            await ctx.send(embed=shipFunction(21, 'AEGIS', aegisColour))

    @bot.command(pass_context=True)
    async def 이드리스m(self, ctx):
        await ctx.send(embed=shipFunction(20, 'AEGIS', aegisColour))

    @bot.command(pass_context=True)
    async def 이드리스p(self, ctx):
        await ctx.send(embed=shipFunction(21, 'AEGIS', aegisColour))

    @bot.command(pass_context=True)
    async def 이드리스k(self, ctx):
        await ctx.send(embed=shipFunction(19, 'AEGIS', aegisColour))



    @cog_ext.cog_slash(name='해머헤드', description='세부함선 없음',guild_ids=[960397196145078333])
    async def _해머헤드(self, ctx: SlashContext):
        await ctx.send(embed = shipFunction(24, 'AEGIS', aegisColour))

    @bot.command(pass_context=True)
    async def 해머헤드(self, ctx):
        await ctx.send(embed=shipFunction(24, 'AEGIS', aegisColour))

    @bot.command(pass_context=True)
    async def 헤머헤드(self, ctx):
        await ctx.send(embed=shipFunction(24, 'AEGIS', aegisColour))

    @bot.command(pass_context=True)
    async def 해머해드(self, ctx):
        await ctx.send(embed=shipFunction(24, 'AEGIS', aegisColour))



    @cog_ext.cog_slash(name='노틸러스', description='세부함선 없음',guild_ids=[960397196145078333])
    async def _노틸러스(self, ctx: SlashContext):
        await ctx.send(embed=shipFunction(4, 'AEGIS', aegisColour))

    @bot.command(pass_context=True)
    async def 노틸러스(self, ctx):
        await ctx.send(embed=shipFunction(4, 'AEGIS', aegisColour))

    @cog_ext.cog_slash(name='리탈리에이터',
                       description='세부함선: 리탈리에이터 베이스, 리탈리에이터 봄버',
                       guild_ids=[960397196145078333],
                       options=[
                           create_option(
                               name='세부함선 명',
                               description='세부함선명을 골라주세요',
                               required=True,
                               option_type=3,
                               choices=[create_choice(name='베이스', value='베이스'),
                                        create_choice(name='봄버', value='봄버')]
                           )
                       ]
                       )
    async def 리탈리에이터(self, ctx: SlashContext, 세부함선: str):
        if  세부함선 == "베이스":
            await ctx.send(embed=shipFunction(7, 'AEGIS', aegisColour))
        elif 세부함선 == "봄버":
            await ctx.send(embed=shipFunction(8, 'AEGIS', aegisColour))
    @bot.command(pass_context=True)
    async def 리탈리에이터(self, ctx, *retali):
        retali = list(retali)
        retali = "".join(retali)
        if retali == "베이스":
            await ctx.send(embed=shipFunction(7, 'AEGIS', aegisColour))
        elif retali == "봄버":
            await ctx.send(embed=shipFunction(8, 'AEGIS', aegisColour))

    @bot.command(pass_context=True)
    async def 리탈리(self, ctx, *retali):
        retali = list(retali)
        retali = "".join(retali)
        if retali == "베이스":
            await ctx.send(embed=shipFunction(7, 'AEGIS', aegisColour))
        elif retali == "봄버":
            await ctx.send(embed=shipFunction(8, 'AEGIS', aegisColour))

    @bot.command(pass_context=True)
    async def 리탈리베이스(self, ctx):
        await ctx.send(embed=shipFunction(7, 'AEGIS', aegisColour))

    @bot.command(pass_context=True)
    async def 베이스(self, ctx):
        await ctx.send(embed=shipFunction(7, 'AEGIS', aegisColour))

    @bot.command(pass_context=True)
    async def 리탈리봄버(self, ctx):
        await ctx.send(embed=shipFunction(8, 'AEGIS', aegisColour))

    @bot.command(pass_context=True)
    async def 봄버(self, ctx):
        await ctx.send(embed=shipFunction(8, 'AEGIS', aegisColour))



    @cog_ext.cog_slash(name='리디머', description='세부함선 없음',guild_ids=[960397196145078333])
    async def _리디머 (self, ctx: SlashContext):
        await ctx.send(embed=shipFunction(5, 'AEGIS', aegisColour))

    @bot.command(pass_context=True)
    async def 리디머(self, ctx):
        await ctx.send(embed=shipFunction(5, 'AEGIS', aegisColour))

    @cog_ext.cog_slash(name='뱅가드',
                       description='세부함선: 뱅가드 센티넬,  뱅가드 워든, 뱅가드 하빈저, 뱅가드 홉라이트',
                       guild_ids=[960397196145078333],
                       options=[
                           create_option(
                               name='세부함선 명',
                               description='세부함선명을 골라주세요',
                               required=True,
                               option_type=3,
                               choices=[create_choice(name='센티넬', value='센티넬'),
                                        create_choice(name='워든', value='워든'),
                                        create_choice(name='하빈저', value='하빈저'),
                                        create_choice(name='홉라이트', value='홉라이트'),
                                        create_choice(name='', value='none')]
                           )
                       ]
                       )
    async def _뱅가드(self, ctx: SlashContext, 세부함선: str):
        if 세부함선  == "워든":
            await ctx.send(embed=shipFunction(10, 'AEGIS', aegisColour))
        elif 세부함선  == "센티넬":
            await ctx.send(embed=shipFunction(9, 'AEGIS', aegisColour))
        elif 세부함선  == "하빈저":
            await ctx.send(embed=shipFunction(11, 'AEGIS', aegisColour))
        elif 세부함선  == "홉라이트":
            await ctx.send(embed=shipFunction(12, 'AEGIS', aegisColour))
        else:
            await ctx.send(embed=serisFunction(26, 'AEGIS', aegisColour))


    @bot.command(pass_context=True)
    async def 뱅가드(self, ctx, *vanguard):
        vanguard = list(vanguard)
        vanguard = "".join(vanguard)
        if vanguard == "워든":
            await ctx.send(embed=shipFunction(10, 'AEGIS', aegisColour))
        elif vanguard == "센티넬":
            await ctx.send(embed=shipFunction(9, 'AEGIS', aegisColour))
        elif vanguard == "하빈저":
            await ctx.send(embed=shipFunction(11, 'AEGIS', aegisColour))
        elif vanguard == "홉라이트":
            await ctx.send(embed=shipFunction(12, 'AEGIS', aegisColour))
        else:
            await ctx.send(embed=serisFunction(26, 'AEGIS', aegisColour))

    @bot.command(pass_context=True)
    async def 뱅가드워든(self, ctx):
        await ctx.send(embed=shipFunction(10, 'AEGIS', aegisColour))

    @bot.command(pass_context=True)
    async def 워든(self, ctx):
        await ctx.send(embed=shipFunction(10, 'AEGIS', aegisColour))

    @bot.command(pass_context=True)
    async def 뱅가드센티넬(self, ctx):
        await ctx.send(embed=shipFunction(9, 'AEGIS', aegisColour))

    @bot.command(pass_context=True)
    async def 센티넬(self, ctx):
        await ctx.send(embed=shipFunction(9, 'AEGIS', aegisColour))

    @bot.command(pass_context=True)
    async def 뱅가드하빈저(self, ctx):
        await ctx.send(embed=shipFunction(11, 'AEGIS', aegisColour))

    @bot.command(pass_context=True)
    async def 하빈저(self, ctx):
        await ctx.send(embed=shipFunction(11, 'AEGIS', aegisColour))

    @bot.command(pass_context=True)
    async def 뱅가드홉라이트(self, ctx):
        await ctx.send(embed=shipFunction(12, 'AEGIS', aegisColour))

    @bot.command(pass_context=True)
    async def 홉라이트(self, ctx):
        await ctx.send(embed=shipFunction(12, 'AEGIS', aegisColour))

    @cog_ext.cog_slash(name='이클립스', description='세부함선 없음',guild_ids=[960397196145078333])
    async def _이클립스(self, ctx: SlashContext):
        embed = shipFunction(22, 'AEGIS', aegisColour)
        await ctx.send(embeds=[embed])
    @bot.command(pass_context=True)
    async def 이클립스(self, ctx):
        await ctx.send(embed=shipFunction(22, 'AEGIS', aegisColour))


    @cog_ext.cog_slash(name='세이버',
                       description='세부함선: 세이버, 세이버 레이븐',
                       guild_ids=[960397196145078333],
                       options=[
                           create_option(
                               name='세부함선 명',
                               description='세부함선명을 골라주세요',
                               required=True,
                               option_type=3,
                               choices=[create_choice(name=' ', value='none'),
                                        create_choice(name='레이븐', value='레이븐')
                                       ]
                           )
                       ]
                       )
    async def _세이버(self, ctx: SlashContext, 세부함선: str):
        if 세부함선 == "레이븐":
            await ctx.send(embed=shipFunction(15, 'AEGIS', aegisColour))
        else:
            await ctx.send(embed=shipFunction(14, 'AEGIS', aegisColour))
    @bot.command(pass_context=True)
    async def 세이버레이븐(self, ctx):
        await ctx.send(embed=shipFunction(15, 'AEGIS', aegisColour))

    @bot.command(pass_context=True)
    async def 레이븐(self, ctx):
        await ctx.send(embed=shipFunction(15, 'AEGIS', aegisColour))

    @bot.command(pass_context=True)
    async def 세이버(self, ctx, *sabre):
        sabre = list(sabre)
        sabre = "".join(sabre)
        if sabre == "레이븐":
            await ctx.send(embed=shipFunction(15, 'AEGIS', aegisColour))
        else:
            await ctx.send(embed=shipFunction(14, 'AEGIS', aegisColour))

    @cog_ext.cog_slash(name='글라디우스',
                       description='세부함선: 글라디우스, 글라디우스 발리언트, 글라디우스 해적판',
                       guild_ids=[960397196145078333],
                       options=[
                           create_option(
                               name='세부함선 명',
                               description='세부함선명을 골라주세요',
                               required=True,
                               option_type=3,
                               choices=[create_choice(name=' ', value='none'),
                                        create_choice(name='발리언트', value='발리언트'),
                                        create_choice(name='해적판', value='해적판')
                                        ]
                           )
                       ]
                       )
    async def _글라디우스(self, ctx: SlashContext, 세부함선: str):
        if 세부함선 == "발리언트":
            await ctx.send(embed=shipFunction(30, 'AEGIS', aegisColour))
        elif 세부함선 == "해적판":
            await ctx.send(embed=shipFunction(31, 'AEGIS', aegisColour))
        else:
            await ctx.send(embed=shipFunction(3, 'AEGIS', aegisColour))

    @bot.command(pass_context=True)
    async def 글라디우스(self, ctx):
        await ctx.send(embed=shipFunction(3, 'AEGIS', aegisColour))

    @bot.command(pass_context=True)
    async def 글라디(self, ctx):
        await ctx.send(embed=shipFunction(3, 'AEGIS', aegisColour))
    @bot.command(pass_context=True)
    async def 글라발리(self, ctx):
        await ctx.send(embed=shipFunction(30, 'AEGIS', aegisColour))
    @bot.command(pass_context=True)
    async def 해적글라디(self, ctx):
        await ctx.send(embed=shipFunction(31, 'AEGIS', aegisColour))
    @bot.command(pass_context=True)
    async def 글라디우스발리언트(self, ctx):
        await ctx.send(embed=shipFunction(30, 'AEGIS', aegisColour))
    @bot.command(pass_context=True)
    async def 해적글라디우스(self, ctx):
        await ctx.send(embed=shipFunction(31, 'AEGIS', aegisColour))

    @cog_ext.cog_slash(name='어벤저',
                       description='세부함선: 어벤저 스토커, 어벤저 타이탄,어벤저 워록,어벤저 레니게이드',
                       guild_ids=[960397196145078333],
                       options=[
                           create_option(
                               name='세부함선 명',
                               description='세부함선명을 골라주세요',
                               required=True,
                               option_type=3,
                               choices=[create_choice(name='스토커', value='스토커'),
                                        create_choice(name='타이탄', value='타이탄'),
                                        create_choice(name='워록', value='워록'),
                                        create_choice(name='레니게이드', value='레니게이드'),
                                        create_choice(name=' ', value='none'),
                                        ]
                           )
                       ]
                       )
    async def _어벤저(self, ctx: SlashContext, 세부함선: str):
        if 세부함선 == "스토커":
            await ctx.send(embed=shipFunction(16, 'AEGIS', aegisColour))
        elif 세부함선 == "타이탄":
            await ctx.send(embed=shipFunction(18, 'AEGIS', aegisColour))
        elif 세부함선 == "워록":
            await ctx.send(embed=shipFunction(17, 'AEGIS', aegisColour))
        elif 세부함선 == "레니게이드":
            await ctx.send(embed=shipFunction(29, 'AEGIS', aegisColour))
        else:
            await ctx.send(embed=serisFunction(27, 'AEGIS', aegisColour))


    @bot.command(pass_context=True)
    async def 어벤져(self, ctx, *avenger):
        avenger = list(avenger)
        avenger = "".join(avenger)
        if avenger == "스토커":
            await ctx.send(embed=shipFunction(16, 'AEGIS', aegisColour))
        elif avenger == "타이탄":
            await ctx.send(embed=shipFunction(18, 'AEGIS', aegisColour))
        elif avenger == "워록":
            await ctx.send(embed=shipFunction(17, 'AEGIS', aegisColour))
        elif avenger == "레니게이드":
            await ctx.send(embed=shipFunction(29, 'AEGIS', aegisColour))
        else:
            await ctx.send(embed=serisFunction(27, 'AEGIS', aegisColour))

    @bot.command(pass_context=True)
    async def 어벤저(self, ctx, *avenger):
        avenger = list(avenger)
        avenger = "".join(avenger)
        if avenger == "스토커":
            await ctx.send(embed=shipFunction(16, 'AEGIS', aegisColour))
        elif avenger == "타이탄":
            await ctx.send(embed=shipFunction(18, 'AEGIS', aegisColour))
        elif avenger == "워록":
            await ctx.send(embed=shipFunction(17, 'AEGIS', aegisColour))
        elif avenger == "레니게이드":
            await ctx.send(embed=shipFunction(29, 'AEGIS', aegisColour))
        else:
            await ctx.send(embed=serisFunction(27, 'AEGIS', aegisColour))

    @bot.command(pass_context=True)
    async def 어벤저스토커(self, ctx):
        await ctx.send(embed=shipFunction(16, 'AEGIS', aegisColour))

    @bot.command(pass_context=True)
    async def 어벤져스토커(self, ctx):
        await ctx.send(embed=shipFunction(16, 'AEGIS', aegisColour))

    @bot.command(pass_context=True)
    async def 스토커(self, ctx):
        await ctx.send(embed=shipFunction(16, 'AEGIS', aegisColour))

    @bot.command(pass_context=True)
    async def 어벤저타이탄(self, ctx):
        await ctx.send(embed=shipFunction(18, 'AEGIS', aegisColour))

    @bot.command(pass_context=True)
    async def 어벤져타이탄(self, ctx):
        await ctx.send(embed=shipFunction(18, 'AEGIS', aegisColour))

    @bot.command(pass_context=True)
    async def 타이탄(self, ctx):
        await ctx.send(embed=shipFunction(18, 'AEGIS', aegisColour))

    @bot.command(pass_context=True)
    async def 어벤저워록(self, ctx):
        await ctx.send(embed=shipFunction(17, 'AEGIS', aegisColour))

    @bot.command(pass_context=True)
    async def 어벤져워록(self, ctx):
        await ctx.send(embed=shipFunction(17, 'AEGIS', aegisColour))

    @bot.command(pass_context=True)
    async def 워록(self, ctx):
        await ctx.send(embed=shipFunction(17, 'AEGIS', aegisColour))

    @bot.command(pass_context=True)
    async def 어벤저레니게이드(self, ctx):
        await ctx.send(embed=shipFunction(29, 'AEGIS', aegisColour))

    @bot.command(pass_context=True)
    async def 어벤져레니게이드(self, ctx):
        await ctx.send(embed=shipFunction(29, 'AEGIS', aegisColour))



    @cog_ext.cog_slash(name='리클레이머', description='세부함선 없음',guild_ids=[960397196145078333])
    async def _리클레이머(self, ctx: SlashContext):
        embed = shipFunction(6, 'AEGIS', aegisColour)
        await ctx.send(embeds=[embed])

    @bot.command(pass_context=True)
    async def 리클레이머(self, ctx):
        await ctx.send(embed=shipFunction(6, 'AEGIS', aegisColour))



    @cog_ext.cog_slash(name='벌칸', description='세부함선 없음',guild_ids=[960397196145078333])
    async def _벌칸(self, ctx: SlashContext):
        embed = shipFunction(13, 'AEGIS', aegisColour)
        await ctx.send(embeds=[embed])
    @bot.command(pass_context=True)
    async def 벌칸(self, ctx):
        await ctx.send(embed=shipFunction(13, 'AEGIS', aegisColour))


def setup(bot):
    bot.add_cog(AEGIS(bot))
