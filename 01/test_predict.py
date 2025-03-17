import unittest
from predict_message import predict_message_mood, MessageModel


class TestMessageModel(unittest.TestCase):
    def test_init(self):
        msg = MessageModel()
        self.assertEqual("Месси", msg.messi)
        self.assertEqual("Роналду", msg.ronaldo)

    def test_mood(self):
        ans = predict_message_mood("Месси")
        self.assertEqual(ans, "отл")

    def test_mod(self):
        ans = predict_message_mood("Роналду")
        self.assertEqual(ans, "отл")

    def test_norm(self):
        ans = predict_message_mood("Старк")
        self.assertEqual(ans, "норм")

    def test_neud(self):
        ans = predict_message_mood("АА")
        self.assertEqual(ans, "неуд")

    def test_error(self):
        with self.assertRaises(TypeError):
            predict_message_mood(1)
