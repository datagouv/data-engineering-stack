import json
import logging
from typing import Optional

import requests
from airflow.models import BaseOperator


class ElasticCreateIndexOperator(BaseOperator):
    """
    Create elasticsearch Index
    :param elastic_url: endpoint url of elasticsearch
    :type elastic_url: str
    :param elastic_index: index to create
    :type elastic_index: str
    :param elastic_index_shards: number of shards for index
    :type elastic_index_shards: int
    :param elastic_user: user for elasticsearch
    :type elastic_user: str
    :param elastic_password: password for elasticsearch
    :type elastic_password: str
    """

    supports_lineage = True

    template_fields = (
        "elastic_url",
        "elastic_index",
        "elastic_user",
        "elastic_password",
        "elastic_index_shards",
    )

    def __init__(
            self,
            *,
            elastic_url: Optional[str] = None,
            elastic_index: Optional[str] = None,
            elastic_user: Optional[str] = None,
            elastic_password: Optional[str] = None,
            elastic_index_shards: Optional[str] = None,
            **kwargs,
    ) -> None:
        super().__init__(**kwargs)

        self.elastic_url = elastic_url
        self.elastic_index = elastic_index
        self.elastic_user = elastic_user
        self.elastic_password = elastic_password
        self.elastic_index_shards = elastic_index_shards

    def execute(self, context):
        if not self.elastic_url:
            raise ValueError("Please provide elasticsearch url endpoint")

        try:
            r = requests.delete(
                self.elastic_url + self.elastic_index,
                auth=(self.elastic_user, self.elastic_password),
            )
        except (requests.exceptions.ConnectionError,
                requests.exceptions.RequestException):
            pass

        if self.elastic_index_shards is not None:
            settings = {
                "settings": {"index": {"number_of_shards": self.elastic_index_shards}}
            }
        else:
            settings = {}

        headers = {"Content-Type": "application/json"}

        r = requests.put(
            self.elastic_url + self.elastic_index,
            headers=headers,
            data=json.dumps(settings),
            auth=(self.elastic_user, self.elastic_password),
        )

        logging.info(r.json())
        assert r.json()["acknowledged"] is True
