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

USER airflow
RUN pip install --upgrade pip
ADD requirements.txt .
RUN pip install apache-airflow==${AIRFLOW_VERSION} -r requirements.txt
