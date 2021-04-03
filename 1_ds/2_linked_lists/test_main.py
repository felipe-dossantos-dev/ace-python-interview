from main import LinkedList


def test_insert_at_tail():
    lst = LinkedList()
    lst.insert_at_tail(0)
    assert str(lst) == "0 -> None"

    lst.insert_at_tail(1)
    assert str(lst) == "0 -> 1 -> None"

    lst.insert_at_tail(2)
    assert str(lst) == "0 -> 1 -> 2 -> None"

    lst.insert_at_tail(3)
    assert str(lst) == "0 -> 1 -> 2 -> 3 -> None"