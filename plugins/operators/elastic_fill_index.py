from typing import Dict, Optional

from airflow.models import BaseOperator
import requests
from requests.auth import HTTPBasicAuth
import logging
import pandas as pd
from minio import Minio
import json


class ElasticFillIndexOperator(BaseOperator):
    """
    Fill elasticsearch Index
    :param elastic_url: endpoint url of elasticsearch
    :type elastic_url: str
    :param elastic_index: index to create
    :type elastic_index: str
    :param elastic_user: user for elasticsearch
    :type elastic_user: str
    :param elastic_password: password for elasticsearch
    :type elastic_password: str
    :param minio_url: minio url where report should be store
    :type minio_url: str
    :param minio_bucket: minio bucket where report should be store
    :type minio_bucket: str
    :param minio_user: minio user which will store report
    :type minio_user: str
    :param minio_password: minio password of minio user
    :type minio_password: str
    :param minio_filepath: complete filepath where to store report
    :type minio_filepath: str
    :param column_id: column which will be used for id in elasticsearch
    :type column_id: str
    """

    supports_lineage = True

    template_fields = ('elastic_url', 'elastic_index', 'elastic_user', 'elastic_password', 'minio_url', 'minio_bucket', 'minio_user', 'minio_password', 'minio_filepath', 'column_id')

    def __init__(
        self,
        *,
        elastic_url: Optional[str] = None,
        elastic_index: Optional[str] = None,
        elastic_user: Optional[str] = None,
        elastic_password: Optional[str] = None,
        minio_url: Optional[str] = None,
        minio_bucket: Optional[str] = None,
        minio_user: Optional[str] = None,
        minio_password: Optional[str] = None,
        minio_filepath: Optional[str] = None,
        column_id: Optional[str] = None,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)

        self.elastic_url = elastic_url
        self.elastic_index = elastic_index
        self.elastic_user = elastic_user
        self.elastic_password = elastic_password
        self.minio_url = minio_url
        self.minio_bucket = minio_bucket
        self.minio_user = minio_user
        self.minio_password = minio_password
        self.minio_filepath = minio_filepath
        self.column_id = column_id

    def execute(self, context):
        if not self.elastic_url:
            raise ValueError("Please provide elasticsearch url endpoint")
        
        client = Minio(
            self.minio_url,
            access_key=self.minio_user,
            secret_key=self.minio_password,
            secure=True
        )
        obj = client.get_object(
            self.minio_bucket,
            self.minio_filepath,
        )
        df = pd.read_csv(obj,dtype=str)

        logging.info('Retrieve file ok - '+str(df.shape[0])+' documents to process')

        df['_id'] = df[self.column_id]
        df_as_json = df.to_json(orient='records', lines=True)

        cpt = 0
        final_json_string = ''
        for json_document in df_as_json.split('\n'):
            cpt = cpt + 1
            if(json_document != ''):
                jdict = json.loads(json_document)
                metadata = json.dumps({'index': {'_id': jdict['_id']}})
                jdict.pop('_id')
                final_json_string += metadata + '\n' + json.dumps(jdict) + '\n'
            if(cpt % 100 == 0):
                if(cpt % 10000 == 0): 
                    logging.info(str(cpt)+' indexed documents')
                headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
                r = requests.post(self.elastic_url+self.elastic_index+'/_bulk', data=final_json_string, headers=headers, timeout=60, auth=(self.elastic_user, self.elastic_password))
                final_json_string = ''

        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.post(self.elastic_url+self.elastic_index+'/_bulk', data=final_json_string, headers=headers, timeout=60, auth=(self.elastic_user, self.elastic_password))


