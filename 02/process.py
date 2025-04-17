import json
from typing import Callable


def process_json(
        json_str: str,
        keys: list[str] | None = None,
        tokens: list[str] | None = None,
        callback: Callable[[str, str], None] | None = None
        ) -> str:
    dct = json.loads(json_str)
    if keys is None:
        keys = dct.keys()
    if tokens is None:
        return ""

    tokens_lower = {token.lower() for token in tokens}

    res = ""
    if callback:
        res += "Callback: "

    for key in keys:
        if key in dct:
            value = dct[key].split()
            for word in value:
                if word.lower() in tokens_lower:
                    if callback:
                        res += f"{callback(key, word)}\n"
                    else:
                        res += f"key={key}, token={word}\n"

    return res


def get_result(key: str, token: str) -> str:
    return f"key={key}, token={token}"
