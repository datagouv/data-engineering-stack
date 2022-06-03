import json
import logging
import os
from urllib.request import urlopen

from dotenv import load_dotenv

load_dotenv()

COLOR_URL = os.getenv("COLOR_URL")


def get_next_color():
    try:
        with urlopen(COLOR_URL) as url:
            data = json.loads(url.read().decode())
            next_color = data["NEXT_COLOR"]
            logging.info(f"******************** Next color from file: {next_color}")
            return next_color
    except BaseException as error:
        raise Exception(f"******************** Ouuups Error: {error}")


NEXT_COLOR = get_next_color()
