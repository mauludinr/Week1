
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
Directed Acyclic Graph (DAG) is a list of task that we want to execute, DAG are located in 'airflow/dags' folder, if you cannot found any 'dags' folder there, try create a new folder named 'dags' inside your airflow directory, then fill that folder with your file
    
1. Set up the connection from Airflow(reference: https://airflow.apache.org/docs/apache-airflow/stable/howto/connection.html)
2. Create DAG from python script
3. Try testing it, with this command
       
       # command layout: command subcommand dag_id task_id date
       # example:
       airflow tasks test DAG-1 mysql_extract 2021-10-30
   
5. If you cannnot run it, try changing the permission of it, as example my 'dag_2.py' that has been in 'dags' folder.
     
       cd dags
       chmod 777 dag_2.py
