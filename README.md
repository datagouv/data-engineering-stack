# Infrastructure Airflow

Ce repository a pour objectif de mettre en place rapidement une infrastructure Airflow permettant à chacun de tester son DAG avant mise en production.

L'infrastructure actuelle est basée sur du LocalExecutor (le scheduler, le webserver et worker sont hébergés sur le même container)

## Installation

```
git clone git@github.com:etalab/data-engineering-stack.git
cd data-engineering-stack

# Create directories necessary for Airflow to work
./1_prepareDirs.sh

# Prepare .env file
./2_prepare_env.sh
nano .env
# Edit POSTGRES_USER ; POSTGRES_PASSWORD ; POSTGRES_DB ; AIRFLOW_ADMIN_MAIL ; AIRFLOW_ADMIN_FIRSTNAME ; AIRFLOW_ADMIN_NAME ; AIRFLOW_ADMIN_PASSWORD

# For MacOS with ARM:
# export DOCKER_DEFAULT_PLATFORM="linux/amd64"

# Launch services
docker-compose up --build -d

# After few seconds, you can connect to http://localhost:8080 with login : AIRFLOW_ADMIN_MAIL and password : AIRFLOW_ADMIN_PASSWORD
```

## Refresh dags

```
# Airflow used to have a little time before dag refreshing when dag is created. You can force refreshing with :
./refreshBagDags.sh
```

## Connections

Connections can be created manually or with python scripts `createConn.py` (using Airflow API) inside each projects. You need also to add your ssh key inside `ssh` folder of repository for the container to be able to see it in `/home/airflow/.ssh/` folder of container.
