from process import process_json, print_result
import sys
import os


def test_success(capsys):
    json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}'
    required_keys = ["key1", "KEY2"]
    tokens = ["WORD1", "word2"]
    process_json(json_str, required_keys, tokens)

    captured = capsys.readouterr() 
    expected_output = "key=key1, token=Word1\nkey=key1, token=word2\n"
    
    assert captured.out == expected_output


def test_with_calback(capsys):
    json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}'
    required_keys = ["key1", "KEY2"]
    tokens = ["WORD1", "word2"]
    process_json(json_str, required_keys, tokens)

    captured = capsys.readouterr() 
    expected_output = "key=key1, token=Word1\nkey=key1, token=word2\n"
    
    assert captured.out == expected_output


def test_no_tokens(capsys):
    json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}'
    required_keys = ["key1", "KEY2"]
    tokens = ["WORD1", "word2"]
    process_json(json_str, required_keys)

    captured = capsys.readouterr() 
    expected_output = ""
    
    assert captured.out == expected_output
