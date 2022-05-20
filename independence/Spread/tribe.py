from FunctionFunction import *

vandulColour = SpecisColour['vandulColour']
aopoaColour = SpecisColour['aopoaColour']

class tribe(commands.Cog):

    def __init__(self,bot):
        self.bot=bot

    @bot.command(pass_context=True)
    async def 반둘(self, ctx):
        await ctx.send(embed=speciesFunctionocess(3,'종족' , vandulColour))

    @bot.command(pass_context=True)
    async def 시안(self, ctx):
        await ctx.send(embed=speciesFunction(2, '종족', aopoaColour))

    @bot.command(pass_context=True)
    async def 테바린(self, ctx):
        await ctx.send(embed=speciesFunction(5, '종족', aopoaColour))

    @bot.command(pass_context=True)
    async def 크르탁(self, ctx):
        await ctx.send(embed=speciesFunction(6, '종족', aopoaColour))
def setup(bot):
    bot.add_cog(tribe(bot))