Stonks
========================
#### Stonks utilizes an unofficial Robinhood API (robin_stocks), discord API, and various other tools/imports to create a user-friendly environment for market enthusiasts. 

<img src="https://i.kym-cdn.com/photos/images/original/001/499/826/2f0.png" width="200" height="200">

Table of Contents
=================

<!--ts-->
   * [Discord Commands](#discord-commands)
      * [Commands](#commands)
      * [Price Checker](#price-checker)
      * [Find Specific Option](#find-specific-option)
      * [Check Option Chain](#check-option-chain)
      * [Top/Bottom 5 S&P performing stocks](#top/bottom-5-s&p-performing-stocks)
      * [Portfolio status](#portfolio-status)
      * [Most mentioned stocks](#most-mentioned-stocks)
   * [Features](#features)
      * [Background Loop](#background-loop)
   * [Checklist](#checklist)
<!--te-->

Discord commands
=================

Command prefix = '.'

<a name="commands"></a>
##### Commands - 
Display directory of commands.
***********
    Ex: .commands

    .commands
    - Price checker: Receive the current price on a stock
    EX: .p (arg1), (arg2), ... (argN)
    - Option: Displays stock option information based on ticker, strike, type (call or put), and expiration.
    Ex: .option [stock], [strike]
    Ex: .option [stock], [strike], [type]
    Ex: .option [stock], [strike], [type], [expiration]
     - Option chain: Displays stock option chain information based on ticker, type (call or put), and expiration.
    Ex: .f [stock]
    Ex: .f [stock], [type]
    Ex: .f [stock], [type], [expiration]
    - Top/Bottom 5 S&P performing stocks
    Ex: .spyup
    Ex: .spydown
    - Most mentioned stocks: Maintains a record of mentioned stocks.
    Ex: .used
<a name="price-checker"></a>
##### Price checker - 
Receive the current price on a stock quickly. Condensed to allow mobile users to view it on one line. 
***********
    Ex: .p (arg1)
    EX: .p (arg1), (arg2), ... (argN)

    {during market hours}
    .p estc aapl msft spy 
    ESTC:  $92.31  +0.92% |L: 91.40   H: 93.59
    AAPL: $460.45  +0.18% |L: 455.86  H: 464.36
    MSFT: $210.20  +0.62% |L: 208.91  H: 211.19
    SPY:  $338.10  +0.37% |L: 336.85  H: 338.34

    {during after hours}
    .p estc aapl msft spy
    ESTC:  $91.47  +0.34% |AH: 91.47   +0.00%
    AAPL: $459.63  -0.19% |AH: 455.29  -0.07%
    MSFT: $210.22  +0.63% |AH: 208.82  -0.05%
    SPY:  $338.14  +0.39% |AH: 336.63  -0.07%
<a name="find-specific-option"></a>
##### Find specific option - 
Displays stock option information based on ticker, type (call or put), and expiration. Auto generates closest 'monthly' expiration if expiration is not provided. Also, option type is defaulted to call. Defaults an incorrect provided parameter (type, expiration, strike), notifies the user on the specific wrong input (expiration and strike), and displays a format example.
***********
    Ex: .option [stock], [strike]
    Ex: .option [stock], [strike], [type]
    Ex: .option [stock], [strike], [type], [expiration]

    .option aapl 470
    AAPL 08-21 C $2.19 -18.28%
    Vol:27K OI:16K IV:30% BE:472.19

    .option fb 260 p
    FB 08-21 P $2.20 -22.26%
    Vol:8K  OI:4K IV:34% BE:257.80
    
    .option fb 260 c 2020-08-28
    FB 08-28 C $7.45 +14.97%
    Vol:4K  OI:1K IV:35% BE:267.45
    
    .option fb 265 c 2020-08-282
    Defaulted expiration date to 2020-08-21. YYYY-MM-DD
    Ex: .f [stock], [strike]
    Ex: .f [stock], [strike], [type]
    Ex: .f [stock], [strike], [type], [expiration]
    
    FB 08-21 C $2.44 +26.42%
    Vol:34K  OI:8K IV:37% BE:267.44
    
    .option aapl 230
    Strike price 250 did not exist for AAPL.
    Defaulted strike to 495 (1 ITM).
    
    AAPL 09-18 495C $24.80 +147.26%
    Vol:7K  OI:1K IV:42% BE:519.80
<a name="check-option-chain"></a>
##### Check Option Chain - 
Utilizes an optimized way of discovering option strike prices relative to the stock. Prints out 1 ITM (In-The-Money) option and 3 OTM (Out-The-Money). Works with calls and puts. 
***********
    Ex: .f [stock]
    Ex: .f [stock], [type]
    Ex: .f [stock], [type], [expiration] *Expiration = monthlies only for accurate results.

    .f aapl
    Option chain for AAPL:
    [ITM] AAPL 09-18 495C $24.80 +147.26%
    Vol:7K  OI:1K IV:42% BE:519.80
    ------------------------------------
    1 OTM. AAPL 09-18 500C $22.50 +157.73%
    Vol:22K OI:24K IV:43% BE:522.50
    ------------------------------------
    2 OTM. AAPL 09-18 505C $20.38 +169.93%
    Vol:3K  OI:1K IV:43% BE:525.38
    ------------------------------------
    3 OTM. AAPL 09-18 510C $18.53 +181.61%
    Vol:3K  OI:3K IV:43% BE:528.53
    ------------------------------------

    .f fb p
    Option chain for FB:
    [ITM] FB 09-18 270P $11.63  +11.29%
    Vol:2K  OI:2K IV:33% BE:258.37
    ------------------------------------
    1 OTM. FB 09-18 265P $9.10   +12.62%
    Vol:642 OI:14K IV:34% BE:255.90
    ------------------------------------
    2 OTM. FB 09-18 260P $7.00   +13.27%
    Vol:452 OI:14K IV:34% BE:253.00
    ------------------------------------
    3 OTM. FB 09-18 255P $5.35   +13.83%
    Vol:772  OI:3K IV:35% BE:249.65
    ------------------------------------
    
    .f fb p 2020-10-16
    Option chain for FB:
    [ITM] FB 10-16 270P $16.03   +6.87%
    Vol:67 OI:642 IV:34% BE:253.97
    ------------------------------------
    1 OTM. FB 10-16 265P $13.53   +5.29%
    Vol:75 OI:12K IV:35% BE:251.47
    ------------------------------------
    2 OTM. FB 10-16 260P $11.53   +7.46%
    Vol:188  OI:4K IV:35% BE:248.47
    ------------------------------------
    3 OTM. FB 10-16 255P $9.55    +8.15%
    Vol:266  OI:1K IV:36% BE:245.45
    ------------------------------------
<a name="top/bottom-5-s&p-performing-stocks"></a>
##### Top/Bottom 5 S&P performing stocks - 
Displays out top 5 S&P performers/sinkers for the day. Sorts by market performance, not extended hours.
***********
    Ex: .spyup
    Ex: .spydown

    .spyup
    TGT:  $154.22 +12.65% |AH: $155.24 +0.66%
    FCX:   $14.94  +3.68% |AH: $14.97  +0.2%
    CTL:   $11.29  +3.58% |AH: $11.40 +0.97%
    NCLH:  $15.68  +3.16% |AH: $15.76 +0.51%
    LYV:   $51.56  +2.46% |AH: $51.56  +0.0%

    .spydown
    JKHY: $172.22 -12.87% |AH: $172.88 +0.38%
    TJX:   $54.36  -5.38% |AH: $54.50 +0.26%
    GILD:  $65.70  -4.87% |AH: $65.80 +0.15%
    ROST:  $90.26  -4.28% |AH: $90.26  +0.0%
    REG:   $40.20  -3.87% |AH: $40.20  +0.0%
<a name="portfolio-status"></a>
##### Portfolio status - 
Checks the current balance of the signed in user's portfolio. Currently set to ONLY allow the discord account associated with the ROBINHOOD_USER_ACCOUNT use this command. 
***********
    Ex: .port 

    .port 
    Current Balance:  $87239.96   +2,225.16    +2.62%
    Buying power: $13,242.81
    Option positions:
<a name="most-mentioned-stocks"></a>
##### Most mentioned stocks -
Maintains a record of mentioned stocks (currently on a csv, [stocks_mentioned.csv] updated every 10 minutes) and outputs the top 5 most used stock tickers. 
***********
    Ex: .used

    .used
    Most mentioned stocks:
    AAPL = 29 
    SPY = 29 
    SQ = 20 
    ESTC = 14 
    TSLA = 13

Features
=================
<a name="background-loop"></a>
##### Background Loop -
Displays a sorted list of specified stocks by gain every 15m between market hours. Not displayed before or after, as well as not on weekends or holidays. Stocks pulled through background loop are not added to 'most mentioned stocks'.  
***********
    {during market hours}
    [15M pull] Intraday
    AMZN: $3294.32 +3.52% |L: 3205.82 H: 3296.96
    NFLX: $492.61  +2.13% |L: 482.88  H: 492.79
    GOOGL:$1532.81 +1.09% |L: 1522.00 H: 1536.00
    AAPL: $461.64   +0.7% |L: 456.03  H: 462.00
    SPY:  $338.41  +0.15% |L: 336.61  H: 339.07
    FB:   $260.30  -0.33% |L: 259.26  H: 262.62
    
    {Pre market and after hours pull}
    [15M pull] Pre-market
    AAPL: $462.25  +0.83% |AH: $463.22 +0.21%
    SPY:  $338.64  +0.22% |AH: $338.90 +0.08%
    NFLX: $491.87  +1.97% |AH: $491.98 +0.02%
    FB:   $262.34  +0.45% |AH: $261.90 -0.17%
    GOOGL:$1555.78 +2.61% |AH: $1552.70  -0.2%
    MSFT: $211.49  +0.58% |AH: $210.98 -0.24%
    AMZN: $3312.49 +4.09% |AH: $3302.00 -0.32%

Checklist
=================

### Initial build

- [x] Connect to pyrh
- [x] Create a discord bot
- [x] Have the discord bot output something onto discord.
- [x] Discord bot use pyrh to output something.
- [x] Create a discord command "priceCheck" that triggers on '.p'. Should output the ticker, current price, and percentage difference since market open. 
- [x] Create a discord command "priceCheckList" that triggers on '.pp'. Performs "priceCheck" on a list of tickers. Produces output in a single message. 
- [x] Implement eastern time for hours, minutes, day.
- [x] Create a background loop, when the bot starts up it will print out the SPY price to a channel and the console with a timestamp every 15m during market hours.
- [x] Have background loop account for holiday days (do not post any automatic stock messages on holidays)

### Next steps

- [x] Tweak priceChecker formatting to enhance the aesthetic and allow all information to be posted on a single line. 
- [x] Allow priceChecker to differentiate the current time to output different results depending on if market is open or not. If market is closed, it should outprint the open price, close price, percent difference, after hours price, and percent difference since market close. 
- [x] Implement csv read to 'stocks mentioned' on load up and csv write every 20 minutes while bot is running.
- [x] Add comments and clean up code.
- [x] Add an additional condition check to validateTicker if the stock provided fits the criteria of 1-5 letters, but does not exist. A stock such as TVIX can cause an exception to pop.
- [x] Add a command for implied IV and move for options. 
- [x] Add the '.option' command which displays monthly (third friday) expiry options (if not provided a date) for the call side (if not provided a side). 
- [x] Add a function that calculates the third friday of each month and verifies the current day is not. This could be used to auto generate an expiration date (monthlies).
- [x] Add a function roundPrice, which rounds up/down based on what type of option is desired (call or put).
- [x] Add a validateType function that returns a type that is corrected or defaulted.
- [x] Add a validateExp function that returns an expiration that is provided, if correct or defaulted date.
- [ ] ~~Fix port command, so stock and option positions that the user has is displayed.~~ ***Currently not possible through robin_stocks API.

### Final steps

- [x] Add an option chain command that checks 1 ITM and 3 OTM strikes for any ticker
- [x] Add a validateStrike function that determines if a strike is correct, if not it calls grabStrikeIterator, RoundPrice, and finally grabStrike to produce a strike.
- [x] Add a searchStrikeIterator function that determines a strike price iterator based off of valid option strike entries.
- [x] Add a grabStrikeIterator function that returns a proper strike price iterator.
- [x] Add a grabStrike function that grabs a determined strike price based on strike iterator, iteration, and roundedprice.
