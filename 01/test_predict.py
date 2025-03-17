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
