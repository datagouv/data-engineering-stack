FROM apache/airflow:3.2.1-python3.12

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
# uv ships with the Airflow image, whose packages live in the virtualenv set
# by VIRTUAL_ENV. Sync the locked dependencies of the DAGs into it. --locked
# fails if uv.lock is out of date with pyproject.toml, and --inexact keeps the
# image's packages that are not in the lock. AIRFLOW_VERSION is set
# by the base image: fail the build if uv.lock has another Airflow version.
COPY dags/datagouvfr_data_pipelines/pyproject.toml dags/datagouvfr_data_pipelines/uv.lock ./
RUN uv sync --locked --no-default-groups --no-install-project --inexact --active --no-cache \
 # fail on conflicting dependencies in the virtualenv
 && uv pip check \
 && python -c "import os, airflow; assert airflow.__version__ == os.environ['AIRFLOW_VERSION'], airflow.__version__"
