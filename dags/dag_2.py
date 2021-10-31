from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.mysql_operator import MySqlOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021,10,30),
    'retries': 0,
}

dag = DAG(dag_id='DAG-2',
          default_args=default_args,
          catchup=False,
          schedule_interval='@once')

mysql_extract = MySqlOperator(
    dag=dag,
    mysql_conn_id='airflow_mysql',
    task_id='mysql_extract_data',
    sql=r"""use hr; select * from employees limit 10;"""
)
