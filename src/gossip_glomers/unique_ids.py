#!/usr/bin/env python3

import json
import sys
import uuid
from typing import Callable, TypedDict


class Message(TypedDict):
    src: str
    dest: str
    body: dict


def handle_message(msg: Message, id_generator: Callable = uuid.uuid4) -> dict:
    body = msg["body"]

    if body["type"] == "init":
        return {
            "src": body["node_id"],
            "dest": msg["src"],
            "body": {
                "type": "init_ok",
                "in_reply_to": body["msg_id"],
            },
        }
    elif body["type"] == "generate":
        guid = id_generator()
        return {
            "src": msg["dest"],
            "dest": msg["src"],
            "body": {
                "type": "generate_ok",
                "msg_id": 1,
                "in_reply_to": body["msg_id"],
                "id": str(guid),
            },
        }

    raise TypeError(f"unknown message type: {body['type']}")


if __name__ == "__main__":
    while line := sys.stdin.readline():
        msg = json.loads(line.strip())
        reply = handle_message(msg)
        print(json.dumps(reply), flush=True)
