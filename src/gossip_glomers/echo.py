#!/usr/bin/env python3

import json
import sys
from typing import TypedDict


class Message(TypedDict):
    src: str
    dest: str
    body: dict


def handle_message(msg: Message) -> dict:
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
    elif body["type"] == "echo":
        return {
            "src": msg["dest"],
            "dest": msg["src"],
            "body": {
                "type": "echo_ok",
                "msg_id": 1,
                "in_reply_to": body["msg_id"],
                "echo": body["echo"],
            },
        }

    raise TypeError(f"unknown message type: {body['type']}")


if __name__ == "__main__":
    while line := sys.stdin.readline():
        msg = json.loads(line.strip())
        reply = handle_message(msg)
        print(json.dumps(reply), flush=True)
