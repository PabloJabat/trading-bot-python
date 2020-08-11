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

Then, using ``conda`` you will create an environment using `environment.yml` in 
the project. Run the following command to create the environment. 

    conda env create -f environment.yml 

This will have created a ``TradingBot`` environment will all the necessary 
tool and packages that the project will need. Make sure you active this 
environment every time that you want to run the code. To activate the environemt
simply run this command.

    conda activate TradingBot

After you´ve done that you will need to create an account in Alpaca and 
get a set of credentials to trade with paper money. After you got them you will
need to create a `config.py` containing the credentials. You have 
`example-config.py` as an example to follow for this. 

You can also watch
[this video](https://www.youtube.com/watch?v=GsGeLHTOGAg&t=100s) to learn how to 
create an account and start using the Alpaca API.

The last step is to make sure that you have ``data`` folder inside the project 
directory. This is the folder that will contain the stock data that the code
needs in order to make the decisions.

## Usage

1. Activate the environment:
    
    ``conda activate TradingBot``
    
2. First you need to run ``pull_data.py`` in order to retrieve the stock data. 
    
    ``python pull_data.py``
    
    You should be able to see the ``data`` folder full of csv files with the 
    bars of the last 50 trading days.
    
3. Lastly, but not least you need to run the bot.

    ``python bot.py``
    
Remember that we are trading with paper money and that the account that you have 
set up is "fictitious" and that you can reset the account any time you want.
