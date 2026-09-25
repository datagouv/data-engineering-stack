# Infrastructure Airflow

Ce repository a pour objectif de mettre en place rapidement une infrastructure Airflow permettant à chacun.e de tester son DAG avant mise en production. Il est basé sur le [guide d'initialisation](https://airflow.apache.org/docs/apache-airflow/3.2.1/howto/docker-compose/index.html) d'une instance Airflow (s'y référer pour plus de détails). Version actuelle : 3.2.1 

## Installation

```bash
git clone git@github.com:datagouv/data-engineering-stack.git
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
# If you have kept the default values: http://localhost:8080 and airflow:airflow as user:pwd
```

## Importer les DAGs de data.gouv.fr

```bash
cd dags
git clone git@github.com:datagouv/datagouvfr_data_pipelines.git
```

Patienter quelques minutes pour qu'Airflow détecte les nouveaux DAGs.

Pour installer un environnement de développement pour les DAGs (version de Python, lint, format, tests, pre-commit), lire le README du dépôt des DAGs : `dags/datagouvfr_data_pipelines/README.md`.
