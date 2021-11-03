from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.mysql_operator import MySqlOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2021,10,30),
    'retries': 1,
}

dag = DAG(dag_id='DAG-7',
          default_args=default_args,
          catchup=False,
          schedule_interval='@daily')

mysql_extract = MySqlOperator(
    dag=dag,
    mysql_conn_id='airflow_mysql',
    task_id='mysql_extract',
    sql=r"""use hr; select * from employees limit 10;"""
)

from sqlalchemy import create_engine
import pandas as pd
import os

connection_string = f"root:123123123@127.0.0.1:3306/chinook?charset=utf8"
con_engine1 = create_engine(f'mysql://{connection_string}')

con_engine2 = create_engine('postgresql://postgres:123123123@localhost/postgres')
dag_path = os.getcwd()
column = ["Album","Artist","Customer","Employee","Genre","Invoice","InvoiceLine","MediaType","Playlist","PlaylistTrack","Track"]

def extract_function():
    
    ## extract data 
    df_list = []
    for i in range(len(column)):
        sql_query = f'select * from postgres.public."{column[i]}";'
        df = pd.read_sql_query(sql_query, con=con_engine2)
        df_list.append(df)
    
    writer2 = pd.ExcelWriter(f"{dag_path}/data.xlsx", engine='xlsxwriter')
    
    for i, df in enumerate (df_list):
        df.to_excel(writer2, sheet_name="Sheet" + str(i+1),index=False)
    writer2.save()
     
    
def load_function():
    ## load_data
    
    xls = pd.ExcelFile(f"{dag_path}/data.xlsx")
    list_sheet = xls.sheet_names
    for i in range(len(column)):
        data = xls.parse(list_sheet[i])
        data.to_sql(str(column[i]).lower(), con=con_engine1, if_exists="replace", index=False)

task_1 = PythonOperator(
    dag=dag,
    task_id='extract_function',
    python_callable=extract_function,
)

task_2 = PythonOperator(
    dag=dag,
    task_id='load_function',
    python_callable=load_function,
)
        
        
mysql_extract >> task_1 >> task_2
