import json
import logging
import os
import requests
from dotenv import load_dotenv

load_dotenv()

AIO_URL = os.getenv("AIO_URL")


def get_next_color():
    try:
        response = requests.get(f"{AIO_URL}/colors")
        next_color = json.loads(response.content)["NEXT_COLOR"]
        response.raise_for_status()
        logging.info(f"******************** AIO URL: {AIO_URL}/colors")
        logging.info(f"******************** NEXT COLOR: {next_color}")
        return next_color
    except requests.exceptions.RequestException as error:
        raise Exception("OOps: Error", error)
