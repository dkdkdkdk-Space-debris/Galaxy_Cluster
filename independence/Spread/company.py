from FunctionFunction import *


class com(commands.Cog):

    def __init__(self,bot):
        self.bot=bot

    @bot.command(pass_context=True)
    async def 회사(self, ctx, *arg):
        arg = "".join(arg)
        if arg == "":
            embed = discord.Embed(title='스타시티즌의 기업',
                                  description='기업은 스타시티즌 경제의 근간입니다. \n'
                                              '선박 부품 생산에서 식품 공급에 이르기까지 모든 것은 Star Citizen 세계 어딘가에 있는 회사에서 수행합니다.\n'
                                              ' 각 회사는 수백 년 된 Quantum Drive 제조업체 Tarsus Electronics에서 최근에 설립된 Cubby Blast에 이르기까지 고유한 역사와 배경을 가지고 있습니다.',
                                  colour=discord.Colour.blue())
            embed.add_field(name='**!기업 사용법**',
                            value='!회사 or 기업을 치시고 뒤에\n구체적인 회사명을 적어 주시면 됩니다.',
                            inline=True)
            embed.set_footer(text='Galaxy Cluster')
        else:
            ws = ss.worksheet('기업')
            raw = str(ws.find(arg).row)
            await ctx.send(embed=companyFunction(raw, '기업'))

    @bot.command(pass_context=True)
    async def 기업(self, ctx, *arg):
        arg = "".join(arg)
        if arg == "":
            embed = discord.Embed(title='스타시티즌의 기업',
                                  description='기업은 스타시티즌 경제의 근간입니다. \n'
                                              '선박 부품 생산에서 식품 공급에 이르기까지 모든 것은 Star Citizen 세계 어딘가에 있는 회사에서 수행합니다.\n'
                                              ' 각 회사는 수백 년 된 Quantum Drive 제조업체 Tarsus Electronics에서 최근에 설립된 Cubby Blast에 이르기까지 고유한 역사와 배경을 가지고 있습니다.',
                                  colour=discord.Colour.blue())
            embed.add_field(name='**!기업 사용법**',
                            value='!회사 or 기업을 치시고 뒤에\n구체적인 회사명을 적어 주시면 됩니다.',
                            inline=True)
            embed.set_footer(text='Galaxy Cluster')
        else:
            ws = ss.worksheet('기업')
            raw = str(ws.find(arg).row)
            await ctx.send(embed=companyFunction(raw, '기업'))



def setup(bot):
    bot.add_cog(com(bot))