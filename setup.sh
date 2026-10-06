#! /usr/bin/env bash
set -euo pipefail

chmod -R 777 ./config
mkdir -p dags
mkdir -p logs
chmod -R 777 ./logs
mkdir -p plugins

# Clone the DAGs from data.gouv.fr before starting Airflow so they are
# available when the containers come up. Pull if already present.
DAGS_REPO_DIR="dags/datagouvfr_data_pipelines"
DAGS_REPO_URL="git@github.com:datagouv/datagouvfr_data_pipelines.git"

if [ -d "$DAGS_REPO_DIR/.git" ]; then
  echo "DAGs repository already present, updating it..."
  git -C "$DAGS_REPO_DIR" pull
else
  echo "Cloning DAGs repository..."
  git clone "$DAGS_REPO_URL" "$DAGS_REPO_DIR"
fi
