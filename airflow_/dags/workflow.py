# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 01:54:51 2021

@author: viswa
"""

from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
import sys
import os
import pandas as pd
import json
print(os.path.abspath("working.............................."))
sys.path.append(os.path.abspath("includes"))

from Extractor import Extractor
extract = Extractor()

def run_extractor(**context):
    sample = extract.load_csv("~/data/sample.csv")
    cleaned = extract.restructure(sample)
    path = "~/data/interim.csv"
    cleaned.to_csv(path, index=False)
    context['ti'].xcom_push(key='dataframe', value=path)
    print(cleaned.iloc[1,1])
    
    


default_args = {"owner":"airflow","start_date":datetime(2021,3,7)}
with DAG(dag_id="workflow",default_args=default_args,schedule_interval='@daily', catchup=False) as dag:
   
    extract_task= PythonOperator(
        task_id = "extract_task",
        python_callable = run_extractor,
        provide_context=True
        )

extract_task