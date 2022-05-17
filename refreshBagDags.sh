#! /usr/bin/env bash
if [ -f .env ]; then
    # Load Environment Variables
    export $(cat .env | grep -v '#' | sed 's/\r$//' | awk '/=/ {print $1}' )
    echo docker exec -it "airflow-${AIRFLOW_ENV_TYPE}-${AIRFLOW_ENV_NAME}" python -c "from airflow.models import DagBag; d = DagBag();"
    docker exec -it "airflow-${AIRFLOW_ENV_TYPE}-${AIRFLOW_ENV_NAME}" python -c "from airflow.models import DagBag; d = DagBag();"
fi
