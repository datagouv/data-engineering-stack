
FROM apache/airflow:2.10.5-python3.12

ARG AIRFLOW_HOME=/opt/airflow

USER root

RUN apt-get update -y && apt-get install -y \
    git \
    lftp \
    zip \
    wget \
    p7zip-full \
    nano \
    jq \
    libmagic1 \
    build-essential \
    libeccodes-dev \
    && apt-get clean

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
