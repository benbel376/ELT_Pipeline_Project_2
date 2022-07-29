from datetime import datetime, timedelta
import airflow
from airflow import DAG
import sys
import os
sys.path.append(os.path.abspath("includes/python"))
from Migrator import MySqlToPostgreOperator

dag = DAG(
    dag_id="job_trial_user",
    start_date=datetime.today() - timedelta(days=1),
    schedule_interval="0 */4 * * *",
    concurrency=100
)

start = MySqlToPostgreOperator(
    task_id=f"start",
    sql="select * from warehouse.source",
    target_table='warehouse.source',
    identifier='track_id',
    dag=dag,
)