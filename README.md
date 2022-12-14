# Introduction

This repo is an intro to [GoodData Python SDK](https://github.com/gooddata/gooddata-python-sdk). The demo requires you to have Python >= 3.7; that is all you need.

## Set up

### GoodData Environment

The demo is created against the GoodData Python SDK testing environment, which can be started using the following command:

```bash
docker compose up -d
``` 

Feel free to use either cloud or self-hosted version, but be aware that some code snippets might not work because they expect some data.

### Python

```bash
# You can run the following command to create a virtual environment and install requirements

make dev

# After that activate the virtual environment
source .venv/bin/activate
``` 

## Basic operations with [gooddata-sdk](https://github.com/gooddata/gooddata-python-sdk/tree/master/gooddata-sdk)

Notebook [basic.ipynb](notebooks/basic.ipynb) contains basic operations with gooddata-sdk.

The entry point is object `GoodDataSdk`, which provides the following catalogs allowing you to work with GoodData:

* catalog_workspace
* catalog_data_source
* ... and other

For more information, see the documentation:
* [[OLD] Python SDK documentation](https://gooddata-sdk.readthedocs.io/en/stable/)
* [[UPCOMING] Python SDK documentation](https://www.gooddata.com/docs/python-sdk/docs/)


## Operations with [gooddata-pandas](https://github.com/gooddata/gooddata-python-sdk/tree/master/gooddata-pandas)

Notebook [pandas.ipynb](notebooks/pandas.ipynb) contains operations with gooddata-pandas.

The entry point is object `GoodPandas`, which provides two factories – `DataFrameFactory` and `SeriesFactory`.

For more information, see the documentation:
* [GoodPandas Documentation](https://gooddata-pandas.readthedocs.io/en/stable/)
* [Pandas documentation](https://pandas.pydata.org/docs/)

## Advanced operations 

Notebook [advanced.ipynb](notebooks/advanced.ipynb) contains advanced use cases of GoodData Python SDK usage.

## Playground 

File [flask_server.py](files/flask_server.py) contains the implementation of a trivial Flask server, which combines a function presented in the previous chapter.