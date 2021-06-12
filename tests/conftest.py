import pytest
import yaml
import json


@pytest.fixture
def config(config_path="params.yaml"):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config


@pytest.fixture
def in_range(schema_path="in_range.json"):
    with open(schema_path) as json_file:
        schema = json.load(json_file)
    return schema
