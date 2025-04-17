import pytest
from descriptor import MatchEvent


@pytest.mark.parametrize("minute, number, last_name, description", [
    (90, 10, "Месси", "гол"),
    (1, 5, "Рамос", "фол"),
    (120, 10, "Неймар", "замена"),
    (45, 7, "Роналду", "гол"),
])
def test_valid_match_event(minute, number, last_name, description):
    event = MatchEvent(minute, number, last_name, description)
    assert event.minute == minute
    assert event.number == number
    assert event.last_name == last_name
    assert event.description == description


def test_event_fail_minute():
    error_message = "Минуты не могут быть отрицательными"
    with pytest.raises(ValueError, match=error_message):
        MatchEvent(-1, 5, "Рамос", "желтая карточка")

    error_message = "Матч не может длиться больше 120 минут"
    with pytest.raises(ValueError, match=error_message):
        MatchEvent(1000, 5, "Рамос", "желтая карточка")

    error_message = "Ожидается int, получено float"
    with pytest.raises(TypeError, match=error_message):
        MatchEvent(45.1, 5, "Рамос", "желтая карточка")


def test_event_fail_footballer():
    error_message = "Ожидается str, получено int"
    with pytest.raises(TypeError, match=error_message):
        MatchEvent(10, 9, 0, "офсайд")

    error_message = "Фамилия не может быть короче одного символа"
    with pytest.raises(ValueError, match=error_message):
        MatchEvent(10, 9, "", "офсайд")


def test_event_fail_number():
    error_message = "Ожидается int, получено complex"
    with pytest.raises(TypeError, match=error_message):
        MatchEvent(10, 1+2j, "Мбаппе", "пенальти")

    error_message = "Нужно положительное число, получено -9"
    with pytest.raises(ValueError, match=error_message):
        MatchEvent(10, -9, "Мбаппе", "пенальти")


VALID_EVENTS = [
    "гол", "пенальти", "автогол", "замена", "офсайд",
    "желтая карточка", "красная карточка", "фол", "угловой"
]


INVALID_EVENTS = [
    "онсайд", "нарушение", "удар", "штанга", "метеорит",
    "флешка на Б", "нокаут", "тачдаун"
]


@pytest.mark.parametrize("event_type", VALID_EVENTS)
def test_valid_event_types(event_type):
    event = MatchEvent(
        minute=10,
        number=7,
        last_name="Роналду",
        description=event_type
    )
    assert event.description == event_type


@pytest.mark.parametrize("event_type", INVALID_EVENTS)
def test_invalid_event_types(event_type):
    with pytest.raises(ValueError):
        MatchEvent(
            minute=10,
            number=7,
            last_name="Роналду",
            description=event_type
        )


def test_invalid_event():
    error_message = "Тип события должен быть строкой, получено int"
    with pytest.raises(TypeError, match=error_message):
        MatchEvent(10, 7, "Ronaldo", 4)


def test_str():
    event = MatchEvent(90, 10, "Месси", "гол")
    assert str(event) == "90' — #10 Месси (Гол)"
