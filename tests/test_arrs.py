from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get(["shell", 18, True], 0, "test") == "shell"
    assert arrs.get([], -1, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([], 1, 5) == []
    assert arrs.my_slice([1, 2, 3, 4], -4) == [1, 2, 3, 4]
    assert arrs.my_slice([1, 2, 3, 4], -2, -1) == [3]
    assert arrs.my_slice([1, 2, 3]) == [1, 2, 3]
