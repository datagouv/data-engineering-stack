# Infrastructure Airflow

Ce repo a pour objectif de mettre en place rapidement une infrastructure Airflow permettant à chacun de tester son DAG avant mise en production.

L'infrastructure actuelle est basée sur du LocalExecutor (le scheduler, le webserver et worker sont hébergées sur le même container)

## Installation

```
git clone git@gitlab.com:etalab/data-engineering/airflow-stack.git
cd airflow-stack

# Create directory necessary for Airflow to work
./1_prepareDirs.sh

# Optionnal - Download actual dags used in production
# Uncomment in script dag for examples if you want to play with test dags
./2_prepareDagsProd.sh

# Prepare .env file 
./3_prepare_env.sh
nano .env 
# Edit POSTGRES_USER ; POSTGRES_PASSWORD ; POSTGRES_DB ; AIRFLOW_ADMIN_MAIL ; AIRFLOW_ADMIN_FIRSTNAME ; AIRFLOW_ADMIN_NAME ; AIRFLOW_ADMIN_PASSWORD

# Launch services
docker-compose up --build -d
```

## Refresh dags

```
# Airflow used to have a little time before dag refreshing when dag is created. You can force refreshing with :
./refreshBagDags.sh
```