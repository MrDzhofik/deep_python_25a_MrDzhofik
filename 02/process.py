import json
from typing import Callable


def process_json(
        json_str: str,
        keys: list[str] | None = None,
        tokens: list[str] | None = None,
        callback: Callable[[str, str], None] | None = None
        ) -> None:
    dct = json.loads(json_str)
    if keys is None:
        keys = dct.keys()
    if tokens is None:
        return

    tokens_lower = {token.lower() for token in tokens}

    for key in keys:
        if key in dct:
            value = dct[key].split()
            for word in value:
                if word.lower() in tokens_lower:
                    if callback:
                        callback(key, word)
                    else:
                        print(f"key={key}, token={word}")


def print_result(key: str, token: str) -> None:
    print(f"key={key}, token={token}")
