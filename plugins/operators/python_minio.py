import os
from typing import Optional

from airflow.operators.python import PythonOperator
from minio import Minio


class PythonMinioOperator(PythonOperator):
    """
    Executes a Python function and uploads contents of tmp_path to Minio.
    :param tmp_path: tmp path to store report during processing
    :type tmp_path: str
    :param minio_url: minio url where report should be store
    :type minio_url: str
    :param minio_bucket: minio bucket where report should be store
    :type minio_bucket: str
    :param minio_user: minio user which will store report
    :type minio_user: str
    :param minio_password: minio password of minio user
    :type minio_password: str
    :param minio_output_filepath: complete filepath where to store report
    :type minio_output_filepath: str
    """

    template_fields = (
        "tmp_path",
        "minio_url",
        "minio_bucket",
        "minio_user",
        "minio_password",
        "minio_output_filepath",
        *PythonOperator.template_fields,
    )

    def __init__(
        self,
        *,
        tmp_path: Optional[str] = None,
        minio_url: Optional[str] = None,
        minio_bucket: Optional[str] = None,
        minio_user: Optional[str] = None,
        minio_password: Optional[str] = None,
        minio_output_filepath: Optional[str] = None,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)

        self.tmp_path = tmp_path
        self.minio_url = minio_url
        self.minio_bucket = minio_bucket
        self.minio_user = minio_user
        self.minio_password = minio_password
        self.minio_output_filepath = minio_output_filepath

    def execute(self, context):
        os.makedirs(os.path.dirname(self.tmp_path + "output/"), exist_ok=True)

        super().execute(context)

        client = Minio(
            self.minio_url,
            access_key=self.minio_user,
            secret_key=self.minio_password,
            secure=True,
        )

        # check if bucket exists.
        found = client.bucket_exists(self.minio_bucket)
        if found:
            for path, subdirs, files in os.walk(self.tmp_path + "output/"):
                for name in files:
                    print(os.path.join(path, name))
                    isFile = os.path.isfile(os.path.join(path, name))
                    if isFile:
                        client.fput_object(
                            self.minio_bucket,
                            self.minio_output_filepath
                            + os.path.join(path, name).replace(
                                self.tmp_path, ""
                            ),
                            os.path.join(path, name),
                        )
