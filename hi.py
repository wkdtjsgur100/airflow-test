from datetime import datetime
from airflow import DAG
from airflow.providers.sqlite.operators.sqlite import SqliteOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

from pandas import json_normalize

import json


with DAG(dag_id='nft-pipeline',
        schedule_interval='@daily',
        default_args=default_args,
        tags=['nft'],
        catchup=False) as dag:
    
    creating_table = SqliteOperator(
        task_id='creating_table',
        sqlite_conn_id='db_sqlite',
        sql='''
            CREATE TABLE IF NOT EXISTS nfts (
                token_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                image_url TEXT NOT NULL
            )
        '''
    )
