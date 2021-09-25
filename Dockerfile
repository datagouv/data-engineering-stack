FROM apache/airflow

USER root 

ARG AIRFLOW_HOME=/opt/airflow 

ADD dags /opt/airflow/dags 

ADD airflow.cfg /opt/airflow/airflow.cfg

RUN pip install --upgrade pip 

RUN chown -R "airflow:airflow" /opt/airflow/

USER airflow 

RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org boto3

# USER ${AIRFLOW_UID}
USER airflow


ADD requirements.txt /requirements.txt

RUN pip install -r /requirements.txt
