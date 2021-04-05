def remove_even(list):
    return [x for x in list if abs(x) % 2 == 1]


def test_remove_even():
    assert remove_even([1, 2, 4, 5, 10, 6, 3]) == [1, 5, 3]