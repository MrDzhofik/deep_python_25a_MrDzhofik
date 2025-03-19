import unittest
from unittest.mock import mock_open, patch
from io import StringIO
from generator import search_lines


class TestSearchLines(unittest.TestCase):
    def test_basic_functionality(self):
        data = """
        Месси обходит соперников на фланге
        Роналду врывается в штрафную
        Идет прострел на Роналду
        и он заколачивает мяч в ворота!
        """

        file = StringIO(data)
        print(file)
        search_words = ["Месси", "Роналду"]
        stop_words = ["прострел"]

        result = list(search_lines(file, search_words, stop_words))
        expected = ["Месси обходит соперников на фланге",
                    "Роналду врывается в штрафную"]

        self.assertEqual(result, expected)

    def test_no_matches(self):
        data = """
        однажды в студёную зимнюю пору
        я из лесу вышел был сильный мороз
        """

        with patch("builtins.open", mock_open(read_data=data)) as mock_file:
            result = list(search_lines(mock_file(), ["лето"], ["мороз"]))
        expected = []

        self.assertEqual(result, expected)

    def test_stop_word_exclusion(self):
        data = "яблоко вкусное\nгруша сладкая\nбанан жёлтый"

        search_words = ["яблоко", "банан"]
        stop_words = ["банан"]

        with patch("builtins.open", mock_open(read_data=data)) as mock_file:
            result = list(search_lines(mock_file(), search_words, stop_words))
        expected = ["яблоко вкусное"]

        self.assertEqual(result, expected)
