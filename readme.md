
# ETL
Tools:

    Python 3.x.x
    Apache Airflow 2.x.x
    Database (MySQL)
    Ubuntu (OS)
    
Dataset:

    Human Resource Dataset (Database in MySQL)

## Installation
Download Ubuntu

    Enable Windows Subsystem for Linux
    Install Ubuntu in Microsoft Store
    
Install the Airflow

    sudo apt-get install python3-pip
    export SLUGIFY_USES_TEXT_UNIDECODE=yes
    sudo pip3 install apache-airflow
    airflow users create — role Admin — username admin — email admin — firstname admin — lastname admin — password admin
    airflow db init
    airflow webserver -p 8080
    airflow scheduler
    
After you succed the installation, now your airflow webserver is ready, http://localhost:8080/


    
