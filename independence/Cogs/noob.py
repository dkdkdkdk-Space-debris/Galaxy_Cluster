import discord
from discord.ext import commands
fleeticon = 'https://cdn.discordapp.com/attachments/695628083801358396/708318261611200623/300x300orang.png'#아이콘 이미지
aegisColour = discord.Colour.dark_grey()
bot=commands
class Noob(commands.Cog):

    def __init__(self,bot):
        self.bot=bot


    # 부품 개조
    # {

    @bot.command(pass_context=True)
    async def 개조(self, ctx):
        embed = discord.Embed(title='', description='https://www.erkul.games/',
                              colour=discord.Colour.blurple())
        embed.set_image(
            url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQN8k-RIHeysxpWQBXZ9-nobuuWAxM4HGAGvw&usqp=CAU')
        await ctx.send(embed=embed)

    # }

    # 조작법


    # 아이템
    @bot.command(pass_context=True)
    async def 아이템(self, ctx):
        embed = discord.Embed(
            title='스시 아이템 링크입니다',
            description='https://finder.deepspacecrew.com/\n**사용법**\n1. 원하는 아이템 종류 클릭\n2. 아이템 이름 검색\n3. 그럼 모든정보가 나옵니다 위치등등',
            colour=discord.Colour.blurple()
        )

        embed.set_image(url='https://starcitizen.tools/images/b/b3/Mobiglas_rgb_projector.png')
        await ctx.send(embed=embed)

    # 채광 광물


    # 무역



    #############################################팁#########################################################################

    #############################################알바########################################################################



def setup(bot):
    bot.add_cog(Noob(bot))