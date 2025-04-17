from classlist import CustomList


def test_add_list():
    a = CustomList([5, 1, 3, 7])
    b = CustomList([1, 2, 7, 1])
    array = [1, 2, 7, 1]
    c = a + b
    d = a + array
    assert c == [6, 3, 10, 8]
    assert c == d
    assert a == [5, 1, 3, 7]
    assert b == [1, 2, 7, 1]


def test_radd_list():
    a = CustomList([5, 1, 3, 7])
    b = CustomList([1, 2, 7, 1])
    array = [1, 2, 7, 1]
    c = b + a
    d = array + a
    assert c == [6, 3, 10, 8]
    assert c == d
    assert a == [5, 1, 3, 7]
    assert b == [1, 2, 7, 1]


def test_add_list_different():
    a = CustomList([5, 1, 3, 7])
    b = CustomList([1, 2, 7])
    array = [1, 2, 7]
    c = a + b
    d = a + array
    assert c == [6, 3, 10, 7]
    assert c == d
    assert a == [5, 1, 3, 7]
    assert b == [1, 2, 7]


def test_add_int():
    a = CustomList([5, 1, 3, 7])
    b = 10
    c = a + b
    assert c == [15, 11, 13, 17]
    assert a == [5, 1, 3, 7]


def test_sub_list():
    a = CustomList([5, 1, 3, 7])
    b = CustomList([1, 2, 7, 1])
    array = [1, 2, 7, 1]
    c = a - b
    d = a - array
    assert c == [4, -1, -4, 6]
    assert c == d
    assert a == [5, 1, 3, 7]
    assert b == [1, 2, 7, 1]


def test_sub_list_different():
    a = CustomList([5, 1, 3, 7])
    b = CustomList([1, 2, 7])
    array = [1, 2, 7]
    c = a - b
    d = a - array
    e = array - a
    assert e == [-4, 1, 4, -7]
    assert c == [4, -1, -4, 7]
    assert c == d
    assert a == [5, 1, 3, 7]
    assert b == [1, 2, 7]


def test_sub_int():
    a = CustomList([5, 1, 3, 7])
    b = 10
    c = a - b
    assert c == [-5, -9, -7, -3]
    assert a == [5, 1, 3, 7]


def test_rsub_int():
    a = CustomList([5, 1, 3, 7])
    b = 10
    c = b - a
    assert c == [5, 9, 7, 3]


def test_eq_list():
    a = CustomList([5, 1])
    b = CustomList([5, 1])
    assert a == b


def test_eq_list_different():
    a = CustomList([5, 1, 4])
    b = CustomList([5, 1])
    assert not a == b


def test_eq_list_diff():
    a = CustomList([5, 2])
    b = CustomList([5, 1])
    assert not a == b


def test_eq_empty_list():
    a = CustomList([])
    b = []
    assert a == b


def test_eq_list_array():
    a = CustomList([5, 1])
    b = [5, 1]
    assert a == b


def test_ne_list():
    a = CustomList([5, 1, 4])
    b = CustomList([5, 2, 3])
    assert a != b


def test_ne_list_array():
    a = CustomList([5, 1, 4])
    b = [5, 2, 3]
    assert a != b


def test_ne_list_different():
    a = CustomList([5, 1, 4])
    b = CustomList([7, 3])
    assert a != b


def test_gt_list():
    a = CustomList([5, 1, 4])
    b = CustomList([5, 1])
    assert a > b


def test_ge_list():
    a = CustomList([5, 1, 4])
    b = CustomList([5, 1])
    c = CustomList([5, 1, 4])
    assert a >= b
    assert a >= c


def test_lt_list():
    a = CustomList([5, 1, 4])
    b = CustomList([5, 1])
    assert b < a


def test_le_list():
    a = CustomList([5, 1, 1])
    b = CustomList([5, 3])
    c = CustomList([5, 1, 4])
    assert a <= b
    assert a <= c


def test_str():
    a = CustomList([5, 1, 4])
    assert str(a) == "[5, 1, 4], sum: 10"
