from process import process_json, get_result


def test_success():
    json_str = """{
    "key1": "Word1 word2",
    "key2": "word2 word3"
    }"""
    required_keys = ["key1", "KEY2"]
    tokens = ["WORD1", "word2"]
    res = process_json(json_str, required_keys, tokens)

    expected_output = "key=key1, token=Word1\nkey=key1, token=word2\n"

    assert res == expected_output


def test_with_calback():
    json_str = """{
    "key1": "Word1 word2",
    "key2": "word2 word3"
    }"""
    required_keys = ["key1", "KEY2"]
    tokens = ["WORD1", "word2"]
    res = process_json(json_str, required_keys, tokens, get_result)
    output = "Callback: key=key1, token=Word1\nkey=key1, token=word2\n"

    assert res == output


def test_no_tokens():
    json_str = """{
    "key1": "Word1 word2",
    "key2": "word2 word3"
    }"""
    required_keys = ["key1", "KEY2"]
    res = process_json(json_str, required_keys)
    print(res)

    expected_output = ""

    assert res == expected_output


def test_no_keys():
    json_str = """{
    "Messi": "Lionel",
    "Ronaldo": "Cristiano dus Santos Aveiru",
    "Zlatan": "Ibragimovic"
    }"""
    tokens = ["Lionel", "Cristiano"]
    res = process_json(json_str=json_str, tokens=tokens)

    expected_output = "key=Messi, token=Lionel\nkey=Ronaldo, token=Cristiano\n"

    assert res == expected_output


def test_empty_tokens():
    json_str = """{
    "Messi": "Lionel",
    "Ronaldo": "Cristiano dus Santos Aveiru",
    "Zlatan": "Ibragimovic"
    }"""
    keys = ["Messi", "Ronaldo"]
    tokens = ["", ""]
    res = process_json(json_str=json_str, keys=keys, tokens=tokens)

    expected_output = ""

    assert res == expected_output


def test_empty_keys():
    json_str = """{
    "Messi": "Lionel",
    "Ronaldo": "Cristiano dus Santos Aveiru",
    "Zlatan": "Ibragimovic"
    }"""
    keys = ["", ""]
    tokens = ["Lionel", "Ibragimovic"]
    res = process_json(json_str=json_str, keys=keys, tokens=tokens)

    expected_output = ""

    assert res == expected_output
