
# Installation

  sudo apt-get install python3-pip
  export SLUGIFY_USES_TEXT_UNIDECODE=yes
  sudo pip3 install apache-airflow
  airflow users create — role Admin — username admin — email admin — firstname admin — lastname admin — password admin
  airflow db init
  airflow webserver -p 8080
  airflow scheduler

Airflow webserver is ready -’http://localhost:8080/’!

    solution("code")
