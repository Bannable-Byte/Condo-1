import os

from discord.ext import commands
from dotenv import load_dotenv
import robin_stocks as r

from stocks import stock_controller as s

bot = commands.Bot(command_prefix='.')
load_dotenv()
rhlogin = r.login(username=os.getenv('RH_USER'), password=os.getenv('RH_PASS'))

initExt = [
    'bot.commands.StockCommands',
    'bot.commands.OptionCommands',
    'bot.commands.BotCommands',
    'bot.tasks.Background',
    'bot.commands.MiscCommands',
]

if __name__ == '__main__':
    for ext in initExt:
        try:
            bot.load_extension(ext)
        except Exception as e:
            print('Failed to load extension {}\n{}: {}'.format(ext, type(e).__name__, e))

    s.readStocksMentioned()  # Populate stocks_mentioned dictionary with .csv items
    # a.prepare_Anomalies()  # Populate option value for SPY friday option chain

    bot.run(os.getenv('Nzk2MTcwMjc2NjY4NDQwNTg2.X_UBWg.WaW8Nj-bilb_ic309690q4kjtE4'))
