from pytest import CaptureFixture
from process import process_json, print_result


def test_success(capsys: CaptureFixture[str]):
    json_str = """{
    "key1": "Word1 word2", 
    "key2": "word2 word3"
    }"""
    required_keys = ["key1", "KEY2"]
    tokens = ["WORD1", "word2"]
    process_json(json_str, required_keys, tokens)

    captured = capsys.readouterr()
    expected_output = "key=key1, token=Word1\nkey=key1, token=word2\n"

    assert captured.out == expected_output


def test_with_calback(capsys: CaptureFixture[str]):
    json_str = """{
    "key1": "Word1 word2", 
    "key2": "word2 word3"
    }"""
    required_keys = ["key1", "KEY2"]
    tokens = ["WORD1", "word2"]
    process_json(json_str, required_keys, tokens, print_result)

    captured = capsys.readouterr()
    expected_output = "key=key1, token=Word1\nkey=key1, token=word2\n"

    assert captured.out == expected_output


def test_no_tokens(capsys: CaptureFixture[str]):
    json_str = """{
    "key1": "Word1 word2", 
    "key2": "word2 word3"
    }"""
    required_keys = ["key1", "KEY2"]
    process_json(json_str, required_keys)

    captured = capsys.readouterr()
    expected_output = ""

    assert captured.out == expected_output


def test_no_keys(capsys: CaptureFixture[str]):
    json_str = """{
    "Messi": "Lionel",
    "Ronaldo": "Cristiano dus Santos Aveiru",
    "Zlatan": "Ibragimovic"
    }"""
    tokens = ["Lionel", "Cristiano"]
    process_json(json_str=json_str, tokens=tokens)

    captured = capsys.readouterr()
    expected_output = "key=Messi, token=Lionel\nkey=Ronaldo, token=Cristiano\n"

    assert captured.out == expected_output


def test_empty_tokens(capsys: CaptureFixture[str]):
    json_str = """{
    "Messi": "Lionel",
    "Ronaldo": "Cristiano dus Santos Aveiru",
    "Zlatan": "Ibragimovic"
    }"""
    keys = ["Messi", "Ronaldo"]
    tokens = ["", ""]
    process_json(json_str=json_str, keys=keys, tokens=tokens)

    captured = capsys.readouterr()
    expected_output = ""

    assert captured.out == expected_output


def test_empty_keys(capsys: CaptureFixture[str]):
    json_str = """{
    "Messi": "Lionel",
    "Ronaldo": "Cristiano dus Santos Aveiru",
    "Zlatan": "Ibragimovic"
    }"""
    keys = ["", ""]
    tokens = ["Lionel", "Ibragimovic"]
    process_json(json_str=json_str, keys=keys, tokens=tokens)

    captured = capsys.readouterr()
    expected_output = ""

    assert captured.out == expected_output
