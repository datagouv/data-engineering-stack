import requests
from requests.auth import HTTPBasicAuth

AIRFLOW_URL=""
AIRFLOW_USER=""
AIRFLOW_PASSWORD=""

variables = [
    # Airflow
    { 'key': 'secret_airflow_url', 'value': '' },
    # Mattermost
    { 'key': 'secret_mattermost_datagouv_reporting', 'value': '' },
    { 'key': 'secret_mattermost_datagouv_activites', 'value': '' },
    { 'key': 'secret_mattermost_dataeng_test', 'value': ''},
    # Minio
    { 'key': 'minio_url', 'value': '' },
    { 'key': 'minio_bucket_opendata', 'value': '' },
    { 'key': 'secret_minio_user_opendata', 'value': '' },
    { 'key': 'secret_minio_password_opendata', 'value': '' },
    # Mails
    { 'key': 'secret_mail_datagouv_bot_sender', 'value': '' },
    { 'key': 'secret_mail_datagouv_bot_user', 'value': '' },
    { 'key': 'secret_mail_datagouv_bot_password', 'value': '' },
    { 'key': 'secret_mail_datagouv_bot_recipients_prod', 'value': '' },
    { 'key': 'secret_mail_datagouv_bot_recipients_demo', 'value': '' },
    { 'key': 'secret_api_key_data_gouv', 'value': '' }
]

for variable in variables:
    r = requests.post(AIRFLOW_URL+"/api/v1/variables", json = variable, auth=HTTPBasicAuth(AIRFLOW_USER,AIRFLOW_PASSWORD))
    if(r.status_code != 200):
        print(variable)
    
