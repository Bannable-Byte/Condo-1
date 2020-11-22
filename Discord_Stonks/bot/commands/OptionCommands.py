from discord.ext import commands  # 3rd party package
from Discord_Stonks.stocks import stocks as s
from Discord_Stonks.options import option_daily_flow as flow, option_controller as o


class OptionCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='option')
    async def findOptions(self, ctx, stock, strike, type=None, expir=None):
        """Takes in a stock ticker, strike, an optional expiration date (defaulted to friday expiration [if applicable]),``
         a type (defaulted to call) and prints the information (Strike, price, volume, OI) to discord.

        :param ctx:
        :param stock: {1-5} character stock-ticker.
        :param type: Defaulted to 'call'. Can be either 'call' or 'put'.
        :param expir: Defaulted to 'None'. Represents the expiration date in the format YYYY-MM-DD

        :return:
        """
        if s.validateTicker(stock):
            price = s.tickerPrice(stock)
            if price >= 5:
                res, msg = o.pcOption(stock, strike, type, expir)
                if msg:
                    await ctx.send("```" + msg + '\n' + res + "```")
                else:
                    await ctx.send("```" + res + "```")
            else:
                await ctx.send("```" + stock.upper() + " is not a valid ticker for options.\n" + "```")
        else:
            await ctx.send("```" + stock.upper() + " is not a valid ticker.\n" + "```")

    @commands.command(name='f')
    async def findOptionChain(self, ctx, stock, type=None, expir=None):
        """Takes in a stock ticker, an optional expiration date (defaulted to friday expiration [if applicable]),``
         a type (defaulted to call) and prints the information (Strike, price, volume, OI) on 1 ITM strike and 3 OTM strikes``
         to discord.

        :param ctx:
        :param stock: {1-5} character stock-ticker.
        :param type: Defaulted to 'call'. Can be either 'call' or 'put'.
        :param expir: Defaulted to 'None'. Represents the expiration date in the format YYYY-MM-DD
        :return:
        """
        if s.validateTicker(stock):
            price = s.tickerPrice(stock)
            if price >= 5:
                res = o.pcOptionChain(stock, type, expir, price)
                await ctx.send("```" + res + "```")
            else:
                await ctx.send("```" + stock.upper() + " is not a valid ticker for options.\n" + "```")
        else:
            await ctx.send("```" + stock.upper() + " is not a valid ticker.\n" + "```")

    @commands.command(name='read')
    async def readFridayOptionChain(self, ctx, stock):
        if s.validateTicker(stock):
            price = s.tickerPrice(stock)
            if price >= 5:
                res = flow.mostExpensive(stock)
                await ctx.send("```" + res + "```")
            else:
                await ctx.send("```" + stock.upper() + " is not a valid ticker for options.\n" + "```")
        else:
            await ctx.send("```" + stock.upper() + " is not a valid ticker.\n" + "```")


def setup(bot):
    bot.add_cog(OptionCommands(bot))
