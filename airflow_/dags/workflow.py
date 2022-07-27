from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
import sys
import os
import pandas as pd
import json
print(os.path.abspath("working.............................."))
sys.path.append(os.path.abspath("includes/python"))

from Extractor import Extractor
from Loader import Loader
extract = Extractor()
loader = Loader()

def run_extractor(**context):
    sample = extract.load_csv("~/data/sample.csv")
    cleaned = extract.restructure(sample)
    path = "~/data/interim.csv"
    cleaned.to_csv(path, index=False)
    context['ti'].xcom_push(key='dataframe', value=path)
    print(cleaned.iloc[1,1])

def run_loader(**context):
    path = context['ti'].xcom_pull(key='dataframe')
    data = extract.load_csv(path)
    print(f"..................  {data.columns}")
    try:
        conn, cur = loader.connect_to_server(host="postgres", port=5432, user="warehouse", password="warehouse", dbName="warehouse")
        loader.create_table(cur, "includes/sql/create_source_table.sql", "warehouse")
        loader.insert_into_table(cur, conn, "warehouse", data, "source")
        loader.close_connection(cur, conn)
    except Exception as e:
        print(f"error...: {e}")
    
    


default_args = {"owner":"airflow","start_date":datetime(2021,3,7)}
with DAG(dag_id="workflow",default_args=default_args,schedule_interval='@daily', catchup=False) as dag:
   
    extract_task= PythonOperator(
        task_id = "extract_task",
        python_callable = run_extractor,
        provide_context=True
        )
    load_task = PythonOperator(
        task_id = "load_task",
        python_callable = run_loader,
        provide_context=True
        )

extract_task >> load_task