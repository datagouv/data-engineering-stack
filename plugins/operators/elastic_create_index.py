from typing import Dict, Optional

from airflow.models import BaseOperator
import requests
from requests.auth import HTTPBasicAuth
import logging

class ElasticCreateIndexOperator(BaseOperator):
    """
    Create elasticsearch Index
    :param elastic_url: endpoint url of elasticsearch
    :type elastic_url: str
    :param elastic_index: index to create
    :type elastic_index: str
    :param elastic_user: user for elasticsearch
    :type elastic_user: str
    :param elastic_password: password for elasticsearch
    :type elastic_password: str
    """

    supports_lineage = True

    template_fields = ('elastic_url', 'elastic_index', 'elastic_user', 'elastic_password')

    def __init__(
        self,
        *,
        elastic_url: Optional[str] = None,
        elastic_index: Optional[str] = None,
        elastic_user: Optional[str] = None,
        elastic_password: Optional[str] = None,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)

        self.elastic_url = elastic_url
        self.elastic_index = elastic_index
        self.elastic_user = elastic_user
        self.elastic_password = elastic_password

    def execute(self, context):
        if not self.elastic_url:
            raise ValueError("Please provide elasticsearch url endpoint")

        try:
            r = requests.delete(self.elastic_url+self.elastic_index, auth=(self.elastic_user,self.elastic_password))
        except:
            pass
        r = requests.put(self.elastic_url+self.elastic_index, auth=(self.elastic_user,self.elastic_password))
        logging.info(r.json())
        assert r.json()['acknowledged'] == True