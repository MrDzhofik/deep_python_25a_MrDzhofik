from classlist import CustomList


def test_add_list():
    a = CustomList([5, 1, 3, 7])
    b = CustomList([1, 2, 7, 1])
    c = a + b
    assert c == [6, 3, 10, 8]


def test_add_list_different():
    a = CustomList([5, 1, 3, 7])
    b = CustomList([1, 2, 7])
    c = a + b
    assert c == [6, 3, 10, 7]


def test_add_int():
    a = CustomList([5, 1, 3, 7])
    b = 10
    c = a + b
    assert c == [15, 11, 13, 17]


def test_sub_list():
    a = CustomList([5, 1, 3, 7])
    b = CustomList([1, 2, 7, 1])
    c = a - b
    assert c == [4, -1, -4, 6]


def test_sub_list_different():
    a = CustomList([5, 1, 3, 7])
    b = CustomList([1, 2, 7])
    c = a - b
    assert c == [4, -1, -4, 7]


def test_sub_int():
    a = CustomList([5, 1, 3, 7])
    b = 10
    c = a - b
    assert c == [-5, -9, -7, -3]


def test_rsub_int():
    a = CustomList([5, 1, 3, 7])
    b = 10
    c = b - a
    assert c == [5, 9, 7, 3]


def test_eq_list():
    a = CustomList([5, 1])
    b = CustomList([5, 1])
    assert a == b


def test_ne_list():
    a = CustomList([5, 1, 4])
    b = CustomList([5, 1])
    assert a != b


def test_gt_list():
    a = CustomList([5, 1, 4])
    b = CustomList([5, 1])
    assert a > b


def test_lt_list():
    a = CustomList([5, 1, 4])
    b = CustomList([5, 1])
    assert b < a
