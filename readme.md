
# ETL using Airflow
Tools:

    Python 3.x.x
    Apache Airflow 2.x.x
    Database (MySQL)
    Ubuntu (OS)
    
Dataset:

    Human Resource Dataset (Database in MySQL)

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
Directed Acyclic Graph (DAG) is a list of task that we want to execute, 
    
1. Set up the connection first from Airflow(reference: https://airflow.apache.org/docs/apache-airflow/stable/howto/connection.html)
