from src.interface import (
    load_data,
    make_decisions,
    take_actions,
    remove_outdated_symbols
)

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

from datetime import timedelta


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