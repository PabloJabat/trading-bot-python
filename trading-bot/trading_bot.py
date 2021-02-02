import argparse

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

from pull_data import get_nasdaq_symbols, pull_symbols_data

from datetime import timedelta

import logging

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)

# My TODO-List
# TODO: We need to create a scheduler that only runs the code
# during week days

# Steps of the Trading bot in dummy functions


def load_data():
    """function to pull the data for the trading bot
    """

    LOGGER.info("Starting to load available symbols")
    symbols = get_nasdaq_symbols()
    some_symbols = symbols[:10]
    LOGGER.info("Starting to pull symbols data")
    pull_symbols_data(some_symbols, 10)
    LOGGER.info("finshed pulling data")


def remove_outdated_symbols():
    print("I've removed the symbols info which is outdated")


def make_decisions():
    print("I know which stocks to sell and which ones to buy")


def take_actions():
    print("I've bought and sold the required stocks")


# DAG definition
default_args = {
    'owner': 'pablo',
    'depends_on_past': False,
    'email': ['oablojabat@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    "trading-bot",
    default_args=default_args,
    description="DAG for the Trading Bot",
    schedule_interval=timedelta(days=1),
    start_date=days_ago(10)
)

t1 = PythonOperator(
    task_id="load_data",
    python_callable=load_data,
    dag=dag
)

t2 = PythonOperator(
    task_id="remove_outdated_symbols",
    python_callable=remove_outdated_symbols,
    dag=dag
)

t3 = PythonOperator(
    task_id="make_decisions",
    python_callable=make_decisions,
    dag=dag
)

t4 = PythonOperator(
    task_id="take_actions",
    python_callable=take_actions,
    dag=dag
)

t1 >> t2 >> t3 >> t4