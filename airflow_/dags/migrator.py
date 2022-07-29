from datetime import datetime, timedelta
import airflow
from airflow import DAG
from custom import MySqlToPostgreOperator

dag = DAG(
    dag_id="job_trial_user",
    start_date=datetime.today() - timedelta(days=1),
    schedule_interval="0 */4 * * *",
    concurrency=100
)

start = MySqlToPostgreOperator(
    task_id=f"start",
    sql="select * from user " 
    "where created_at BETWEEN '{start_date}' "
    "AND '{end_date}'",
    target_table='public.user',
    identifier='id',
    dag=dag,
)