class MessageModel:
    def __init__(self):
        self.messi = "Месси"
        self.ronaldo = "Роналду"

    def more(self):
        pass

    def predict(self, message: str) -> float:
        if message in (self.messi, self.ronaldo):
            return 1.0
        return len(message) % 10 / 10


def predict_message_mood(
    message: str,
    bad_thresholds: float = 0.3,
    good_thresholds: float = 0.8,
) -> str:
    model = MessageModel()
    mood = model.predict(message)
    if mood < bad_thresholds:
        return "неуд"
    if mood > good_thresholds:
        return "отл"
    return "норм"

if __name__ == '__main__':
    msg = input("Введите сообщение: ")
    print(predict_message_mood(msg))
