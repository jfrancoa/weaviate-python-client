from typing import Dict, Any

import pytest

import weaviate

GIT_HASH = "977af56"
SERVER_VERSION = "1.23.0-rc.0"
NODE_NAME = "node1"
NUM_OBJECT = 10


def schema(class_name: str) -> Dict[str, Any]:
    return {
        "classes": [
            {
                "class": class_name,
                "properties": [
                    {"dataType": ["string"], "name": "stringProp"},
                    {"dataType": ["int"], "name": "intProp"},
                ],
            }
        ]
    }


@pytest.fixture(scope="module")
def client():
    client = weaviate.Client("http://localhost:8080")
    client.schema.delete_all()
    yield client
    client.schema.delete_all()


def test_get_nodes_status_without_data(client):
    """get nodes status without data"""
    resp = client.cluster.get_nodes_status(output="verbose")
    assert len(resp) == 1
    assert resp[0]["gitHash"] == GIT_HASH
    assert resp[0]["name"] == NODE_NAME
    assert resp[0]["shards"] is None  # no class given
    assert resp[0]["stats"]["objectCount"] == 0
    assert resp[0]["stats"]["shardCount"] == 0
    assert resp[0]["status"] == "HEALTHY"
    assert resp[0]["version"] == SERVER_VERSION


def test_get_nodes_status_with_data(client):
    """get nodes status with data"""
    class_name1 = "ClassA"
    uncap_class_name1 = "classA"
    client.schema.create(schema(class_name1))
    for i in range(NUM_OBJECT):
        client.data_object.create({"stringProp": f"object-{i}", "intProp": i}, class_name1)

    class_name2 = "ClassB"
    client.schema.create(schema(class_name2))
    for i in range(NUM_OBJECT * 2):
        client.data_object.create({"stringProp": f"object-{i}", "intProp": i}, class_name2)

    resp = client.cluster.get_nodes_status(output="verbose")
    assert len(resp) == 1
    assert resp[0]["gitHash"] == GIT_HASH
    assert resp[0]["name"] == NODE_NAME
    assert len(resp[0]["shards"]) == 2
    assert resp[0]["stats"]["objectCount"] == NUM_OBJECT * 3
    assert resp[0]["stats"]["shardCount"] == 2
    assert resp[0]["status"] == "HEALTHY"
    assert resp[0]["version"] == SERVER_VERSION

    shards = sorted(resp[0]["shards"], key=lambda x: x["class"])
    assert shards[0]["class"] == class_name1
    assert shards[0]["objectCount"] == NUM_OBJECT
    assert shards[1]["class"] == class_name2
    assert shards[1]["objectCount"] == NUM_OBJECT * 2

    resp = client.cluster.get_nodes_status(class_name1, "verbose")
    assert len(resp) == 1
    assert resp[0]["gitHash"] == GIT_HASH
    assert resp[0]["name"] == NODE_NAME
    assert len(resp[0]["shards"]) == 1
    assert resp[0]["stats"]["shardCount"] == 1
    assert resp[0]["status"] == "HEALTHY"
    assert resp[0]["version"] == SERVER_VERSION

    assert shards[0]["class"] == class_name1
    assert shards[0]["objectCount"] == NUM_OBJECT
    assert resp[0]["stats"]["objectCount"] == NUM_OBJECT

    resp = client.cluster.get_nodes_status(uncap_class_name1, "verbose")
    assert len(resp) == 1
    assert resp[0]["gitHash"] == GIT_HASH
    assert resp[0]["name"] == NODE_NAME
    assert len(resp[0]["shards"]) == 1
    assert resp[0]["stats"]["shardCount"] == 1
    assert resp[0]["status"] == "HEALTHY"
    assert resp[0]["version"] == SERVER_VERSION

    assert shards[0]["class"] == class_name1
    assert shards[0]["objectCount"] == NUM_OBJECT
    assert resp[0]["stats"]["objectCount"] == NUM_OBJECT
