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
# uv ships with the Airflow image. Install the locked dependencies of the DAGs
# on top of the image. Export uv.lock rather than using uv sync, which would
# uninstall the image's packages that are not in the lock. AIRFLOW_VERSION is
# set by the base image: pinning it makes the build fail if uv.lock was
# resolved with another Airflow version.
COPY dags/datagouvfr_data_pipelines/pyproject.toml dags/datagouvfr_data_pipelines/uv.lock ./
RUN uv export --frozen --no-dev --no-emit-project --no-hashes -o requirements.txt \
 && uv pip install --no-cache apache-airflow==${AIRFLOW_VERSION} -r requirements.txt
