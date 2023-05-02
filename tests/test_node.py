import pytest

from gossip_glomers.node import Init, create_message


def test_create_init_message():
    payload = {
        "src": "src",
        "dest": "dst",
        "body": {
            "type": "init",
            "msg_id": 1,
            "node_id": "n3",
            "node_ids": ["n1", "n2", "n3"],
        },
    }

    init_msg = create_message(payload)

    assert isinstance(init_msg, Init)


def test_init_message_guards():
    payload = {
        "src": "src",
        "dest": "dst",
        "body": {"type": "echo", "msg_id": 1, "echo": "Please echo 35"},
    }

    with pytest.raises(AssertionError):
        Init(**payload)
