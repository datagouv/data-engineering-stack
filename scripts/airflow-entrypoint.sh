#!/usr/bin/env bash
airflow resetdb
airflow db init
airflow upgradedb
airflow users create -r Admin -u geoffrey.aldebert@data.gouv.fr -e geoffrey.aldebert@data.gouv.fr -f Geoffrey -l Aldebert -p 2021etalab123!
airflow scheduler &
airflow webserver

