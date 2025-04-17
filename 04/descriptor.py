from abc import ABC, abstractmethod


class BaseDescriptor(ABC):
    private_name: str

    def __set_name__(self, owner, name):
        self.private_name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name, None)

    def __set__(self, instance, value):
        self._validate(value)
        setattr(instance, self.private_name, value)

    @abstractmethod
    def _validate(self, value):
        return


class Footballer(BaseDescriptor):
    def _validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f"Ожидается str, получено {type(value).__name__}")
        if len(value) == 0:
            raise ValueError("Фамилия не может быть короче одного символа")


class Minute(BaseDescriptor):
    def _validate(self, value):
        if isinstance(value, int):
            if value <= 0:
                raise ValueError("Минуты не могут быть отрицательными")
            if value > 120:
                raise ValueError("Матч не может длиться больше 120 минут")
        else:
            raise TypeError(f"Ожидается int, получено {type(value).__name__}")


class Number(BaseDescriptor):
    def _validate(self, value):
        if isinstance(value, int):
            if value <= 0:
                raise ValueError(
                    f"Нужно положительное число, получено {value}"
                    )
        else:
            raise TypeError(f"Ожидается int, получено {type(value).__name__}")


class EventType(BaseDescriptor):
    EVENTS = {
        "гол", "пенальти", "автогол", "замена", "офсайд",
        "желтая карточка", "красная карточка", "фол", "угловой"
    }

    def _validate(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f"Тип события должен быть строкой, "
                f"получено {type(value).__name__}"
                )
        if value.lower() not in self.EVENTS:
            raise ValueError(
                f"Недопустимое событие. Допустимые: {', '.join(self.EVENTS)}"
                )


class MatchEvent:
    minute = Minute()
    number = Number()
    last_name = Footballer()
    description = EventType()

    def __init__(self, minute, number, last_name, description):
        self.minute = minute
        self.number = number
        self.last_name = last_name
        self.description = description

    def __str__(self):
        return (
            f"{self.minute}' — #{self.number} {self.last_name} "
            f"({self.description.capitalize()})"
        )
