FROM apache/airflow:2.10.5-python3.12

ARG AIRFLOW_HOME=/opt/airflow

USER root

RUN apt-get update -y
RUN apt-get install git -y
RUN apt-get install lftp -y
RUN apt-get install zip -y
RUN apt-get install wget -y
RUN apt-get install p7zip-full -y
RUN apt-get install nano -y
RUN apt-get install jq -y
RUN apt-get install libmagic1 -y

USER airflow

RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org boto3
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

ARG USER_NAME
ARG USER_EMAIL
RUN git config --global user.email "${USER_EMAIL}"
RUN git config --global user.name "${USER_NAME}"

COPY airflow.cfg ${AIRFLOW_HOME}/airflow.cfg
