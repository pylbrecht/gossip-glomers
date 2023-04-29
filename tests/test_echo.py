import pytest

from gossip_glomers.echo import handle_message


@pytest.mark.parametrize(
    "msg,reply",
    [
        (
            {
                "src": "src",
                "dest": "dst",
                "body": {
                    "type": "init",
                    "msg_id": 1,
                    "node_id": "n3",
                    "node_ids": ["n1", "n2", "n3"],
                },
            },
            {
                "type": "init_ok",
                "in_reply_to": 1,
            },
        ),
        (
            {
                "src": "c1",
                "dest": "n1",
                "body": {"type": "echo", "msg_id": 1, "echo": "Please echo 35"},
            },
            {
                "src": "n1",
                "dest": "c1",
                "body": {
                    "type": "echo_ok",
                    "msg_id": 1,
                    "in_reply_to": 1,
                    "echo": "Please echo 35",
                },
            },
        ),
    ],
    ids=["init", "echo"],
)
def test_handle_message(msg, reply):
    assert handle_message(msg) == reply
