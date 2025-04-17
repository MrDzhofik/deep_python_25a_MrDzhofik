import inspect
import pytest
from custom import CustomClass


def test_x():
    inst = CustomClass()
    assert inst.custom_x == 50
    error_message = "'CustomClass' object has no attribute 'x'"
    with pytest.raises(AttributeError, match=error_message):
        return inst.x


def test_val():
    inst = CustomClass()
    assert inst.custom_val == 99
    error_message = "'CustomClass' object has no attribute 'val'"
    with pytest.raises(AttributeError, match=error_message):
        return inst.val


def test_line():
    inst = CustomClass()
    assert inst.custom_line() == 100
    error_message = "'CustomClass' object has no attribute 'line'"
    with pytest.raises(AttributeError, match=error_message):
        return inst.line()


def test_dynamic():
    inst = CustomClass()
    inst.dynamic = "added later"
    assert inst.custom_dynamic == "added later"
    error_message = "'CustomClass' object has no attribute 'dynamic'"
    with pytest.raises(AttributeError, match=error_message):
        return inst.dynamic


def test_str():
    inst = CustomClass()
    assert str(inst) == "Custom_by_metaclass"


def test_magic():
    magic_methods = [
        name for name, _ in inspect.getmembers(CustomClass)
        if name.startswith("__") and name.endswith("__")
    ]

    for method in magic_methods:
        assert not hasattr(CustomClass, f"custom_{method}")
