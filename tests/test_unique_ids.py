import functools
import uuid

import pytest

from gossip_glomers.unique_ids import handle_message


@pytest.fixture
def fake_id_gen():
    return functools.partial(uuid.UUID, int=0)


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
                "src": "n3",
                "dest": "src",
                "body": {
                    "type": "init_ok",
                    "in_reply_to": 1,
                },
            },
        ),
        (
            {
                "src": "c1",
                "dest": "n1",
                "body": {"type": "generate", "msg_id": 1},
            },
            {
                "src": "n1",
                "dest": "c1",
                "body": {
                    "type": "generate_ok",
                    "msg_id": 1,
                    "in_reply_to": 1,
                    "id": "00000000-0000-0000-0000-000000000000",
                },
            },
        ),
    ],
    ids=["init", "generate"],
)
def test_handle_message(msg, reply, fake_id_gen):
    assert handle_message(msg, id_generator=fake_id_gen) == reply
