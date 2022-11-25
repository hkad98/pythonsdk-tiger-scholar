from gooddata_sdk import GoodDataSdk
from gooddata_pandas import GoodPandas
import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    host = os.environ["HOST"]
    token = os.environ["TOKEN"]

    sdk = GoodDataSdk.create(host, token)
    pandas = GoodPandas(host, token)
