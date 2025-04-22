#!/usr/bin/env bash
airflow db reset
airflow db migrate
airflow users create -r Admin -u "$AIRFLOW_ADMIN_MAIL" -e "$AIRFLOW_ADMIN_MAIL" -f "$AIRFLOW_ADMIN_FIRSTNAME" -l "$AIRFLOW_ADMIN_NAME" -p "$AIRFLOW_ADMIN_PASSWORD"
airflow scheduler &
airflow webserver
