FROM apache/airflow:2.9.3-python3.10

USER root

ARG AIRFLOW_HOME=/opt/airflow

ADD airflow.cfg /opt/airflow/airflow.cfg

USER airflow

RUN pip install --upgrade pip

USER root

# MySQL key rotation (https://dev.mysql.com/doc/refman/8.0/en/checking-gpg-signature.html)
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A8D3785C

RUN apt-get update -y
RUN apt-get install git lftp zip wget p7zip-full -y

RUN chown -R "airflow:root" /opt/airflow/

ADD ssh /home/airflow/.ssh/
RUN chown -R airflow:root /home/airflow/.ssh

USER airflow

RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org boto3


# USER ${AIRFLOW_UID}
USER airflow

ADD requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN git config --global user.email "geoffrey.aldebert@data.gouv.fr"
RUN git config --global user.name "Geoffrey Aldebert (Bot Airflow)"
