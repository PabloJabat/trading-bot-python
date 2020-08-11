# Trading Bot

This project aims at building a simple trading bot using python and the
[Alpaca API](https://alpaca.markets/). The bot is designed to use Paper Money
but it could be easily set up to use real money with a few more tweaks.

The algorithm uses two SMA (Simple Moving Averages) to detect when to buy or 
sell stocks as explained in this 
[link](https://www.youtube.com/watch?v=4R2CDbw4g88).

The **main goal** of this project is to **set up the necessary tools and 
ecosystem to be able to simply press run every day and let the bot trade using 
the SMA decisions**. A nice addition would be to have an orchestrator like 
[Apache Airflow](https://airflow.apache.org/) to schedule all this runs 
automatically. 

## Installation

You will first need to clone this project in your machine as shown below.

    git clone https://github.com/PabloJabat/trading-bot-python
    
After you´ve done that you will need to create an account in Alpaca and 
get a set of credentials to trade with paper money. After you got them you will
need to create a `config.py` containing the credentials. You have 
`example-config.py` as an example to follow for this. 

You can also watch
[this video](https://www.youtube.com/watch?v=GsGeLHTOGAg&t=100s) to learn how to 
create an account in alpaca and start using Alpaca API.
