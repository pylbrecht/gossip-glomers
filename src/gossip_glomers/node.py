from dataclasses import dataclass


@dataclass
class Message:
    src: str
    dest: str
    body: dict


@dataclass
class Init(Message):
    def __post_init__(self):
        assert (
            self.body["type"] == "init"
        ), f"expected message type 'init', got {repr(self.body['type'])}"


def create_message(payload: dict) -> Message:
    if payload["body"]["type"] == "init":
        return Init(**payload)
