from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2 # поправил значение на выходе на корректное
    assert arrs.get([], 0, "test") == "test"


def test_my_slice(): # изменил название функции, добавил тестов для 100% покрытия
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4, 5], -3) == [3, 4, 5]
    assert arrs.my_slice([1, 2, 3, 4, 5], -10, 5) == [1, 2, 3, 4, 5]
    assert arrs.my_slice([]) == []