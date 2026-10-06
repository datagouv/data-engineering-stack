# Infrastructure Airflow

Ce repository a pour objectif de mettre en place rapidement une infrastructure Airflow permettant à chacun.e de tester son DAG avant mise en production. Il est basé sur le [guide d'initialisation](https://airflow.apache.org/docs/apache-airflow/3.2.1/howto/docker-compose/index.html) d'une instance Airflow (s'y référer pour plus de détails). Version actuelle : 3.2.1 

## Installation

Cloner et préparer le dépôt :

```bash
git clone git@github.com:datagouv/data-engineering-stack.git
cd data-engineering-stack

# Create directories necessary for Airflow to work
# and clone the data.gouv.fr DAGs (dags/datagouvfr_data_pipelines) so they are
# available before the containers start. Git pull if the repository already exists.
./setup.sh

# Prepare .env file:
# Create a .env file from the .envExample and fill in the required variables.
# You may also add more variables there for specific DAGs to run.
```

Initialiser Airflow (à lancer une fois). Si `docker` tourne dans une machine virtuelle (VM), il faut d'abord se connecter à cette VM pour lancer la commande :

```
docker compose up airflow-init
```

Lancer les services (Airflow) :

```
docker compose up -d
```

Après quelques secondes, Airflow est accessible sur `http://localhost:<AIRFLOW_WEBSERVER_PORT>`. Pour se connecter, login : AIRFLOW_ADMIN_MAIL et mot de passe : AIRFLOW_ADMIN_PASSWORD. Les valeurs par défaut sont http://localhost:8080 et `airflow`/`airflow` pour login et mot de passe.

## DAGs de data.gouv.fr

Le dépôt des DAGs est cloné automatiquement dans `dags/datagouvfr_data_pipelines` par `./setup.sh` (exécuté au-dessus, avant le démarrage des conteneurs). Pour mettre à jour ce dépôt manuellement :

```bash
git -C dags/datagouvfr_data_pipelines pull
```

Pour installer un environnement de développement pour les DAGs (version de Python, lint, format, tests, pre-commit), lire le README du dépôt des DAGs : `dags/datagouvfr_data_pipelines/README.md`.
