FROM apache/airflow

USER root 

ARG AIRFLOW_HOME=/opt/airflow 

ADD dags /opt/airflow/dags 

RUN pip install --upgrade pip 

USER airflow 

RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org boto3

USER ${AIRFLOW_UID}

ADD requirements.txt /requirements.txt

RUN pip install -r /requirements.txt
