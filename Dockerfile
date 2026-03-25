FROM apache/airflow:3.1.7-python3.12

USER root

# MySQL key rotation (https://dev.mysql.com/doc/refman/8.0/en/checking-gpg-signature.html)
# RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A8D3785C

RUN apt-get update -y
RUN apt-get install git -y
RUN apt-get install lftp -y
RUN apt-get install zip -y
RUN apt-get install wget -y
RUN apt-get install p7zip-full -y
RUN apt-get install nano -y
RUN apt-get install jq -y
RUN apt-get install libmagic1 -y
# To build Psycopg for dbt-postgres we need before pip install :
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    libpq-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

#USER airflow
#RUN pip install --upgrade pip
#ADD requirements.txt .
#RUN pip install apache-airflow==${AIRFLOW_VERSION} -r requirements.txt
USER airflow
RUN pip install --upgrade pip setuptools wheel

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
