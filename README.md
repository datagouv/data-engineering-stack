# Infrastructure Airflow

Ce repository a pour objectif de mettre en place rapidement une infrastructure Airflow permettant à chacun.e de tester son DAG avant mise en production. Il est basé sur le [guide d'initialisation](https://airflow.apache.org/docs/apache-airflow/3.1.7/howto/docker-compose/index.html) d'une instance Airflow (s'y référer pour plus de détails). Version actuelle : 3.1.7 

## Installation

```bash
git clone git@github.com:etalab/data-engineering-stack.git
cd data-engineering-stack

# Create directories necessary for Airflow to work
./prepareDirs.sh

# Prepare .env file:
# Create a .env file from the .envExample and fill in the required variables.
# You may also add more variables there for specific DAGs to run.

# Initialize
docker compose up airflow-init

# Launch services
docker compose up -d

# After few seconds, you can connect to http://localhost:<AIRFLOW_WEBSERVER_PORT> with login : AIRFLOW_ADMIN_MAIL and password : AIRFLOW_ADMIN_PASSWORD
```

## Import our DAGs
```bash
cd dags
git clone git@github.com:datagouv/datagouvfr_data_pipelines.git
```

## Refresh dags

```bash
# Airflow used to have a little time before dag refreshing when dag is created. You can force refreshing with :
./refreshBagDags.sh
```
