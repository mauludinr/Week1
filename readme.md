
# ETL using Airflow
Tools:

    Python 3.x.x
    Apache Airflow 2.x.x
    Database (MySQL and PostgreMySQL locally)
    Ubuntu (OS)
    
Dataset:

    Human Resource Dataset (Database in MySQL)
    Chinook Dataset (Database in PostgreSQL)

## Installation Airflow 
Install Ubuntu in Windows

    Enable Windows Subsystem for Linux
    Go to Microsoft Store, download and then install Ubuntu
    
Update python pip
    
    sudo apt-get install software-properties-common
    sudo apt-add-repository universe
    sudo apt-get update
    sudo apt-get install python3-pip
    
Install the Airflow

    export SLUGIFY_USES_TEXT_UNIDECODE=yes
    sudo pip3 install apache-airflow
    airflow users create — role Admin — username admin — email admin — firstname admin — lastname admin — password admin
    airflow db init
    airflow webserver -p 8080
    airflow scheduler
    
After you succed the installation, now your airflow webserver is ready, you can access your airflow GUI from browser in http://localhost:8080/

## Directed Acyclic Graph (DAG) 
Directed Acyclic Graph (DAG) is a list of task that we want to execute, DAG are located in 'airflow/dags' folder, if you cannot found any 'dags' folder there, try create a new folder named 'dags' inside your airflow directory
    
1. Set up the connection from Airflow(reference: https://airflow.apache.org/docs/apache-airflow/stable/howto/connection.html)
2. Try testing dag with specific task, with this command:
       
       # command layout: airflow tasks test [DAG_ID] [TASK_ID] [EXECUTION_DATE]
       # example:
       airflow tasks test DAG-1 mysql_extract 2021-10-30
   
3. If you cannnot run it, try changing the permission of it, as example my 'dag_2.py' that has been in 'dags' folder.
     
       cd dags
       chmod 777 dag_2.py

![ETL_1](https://user-images.githubusercontent.com/38213112/140048194-d6827659-68cf-4bc2-8456-4d6c7db4be5a.png)

![ETL_2](https://user-images.githubusercontent.com/38213112/140048251-b513b67e-4ab5-445f-8673-499ca0b62503.png)
