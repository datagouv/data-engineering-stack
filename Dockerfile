FROM apache/airflow:slim-2.9.3-python3.12

ARG AIRFLOW_HOME=/opt/airflow

USER root

RUN apt-get update -y
RUN apt-get install git lftp zip wget p7zip-full -y

RUN chown -R "airflow:root" /opt/airflow/
ADD ssh /home/airflow/.ssh/
RUN chown -R airflow:root /home/airflow/.ssh

USER airflow

RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org boto3
ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

ARG USER_NAME
ARG USER_EMAIL
RUN git config --global user.email "${USER_EMAIL}"
RUN git config --global user.name "${USER_NAME}"

ADD airflow.cfg /opt/airflow/airflow.cfg
