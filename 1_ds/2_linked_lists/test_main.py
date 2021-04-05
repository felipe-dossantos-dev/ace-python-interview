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


def test_search():
    lst = LinkedList()
    lst.insert_at_tail(5)
    lst.insert_at_tail(90)
    lst.insert_at_tail(10)
    lst.insert_at_tail(4)

    assert not lst.search_recursive(11)
    assert lst.search_recursive(4)

    assert not lst.search(11)
    assert lst.search(4)


def test_delete():
    lst = LinkedList()
    lst.insert_at_tail(5)
    lst.insert_at_tail(90)
    lst.insert_at_tail(10)
    lst.insert_at_tail(4)

    assert lst.delete(5)
    print(lst)
    assert not lst.delete(50)
    assert not lst.delete(5)
    assert lst.delete(4)
    print(lst)
    assert lst.delete(10)
    print(lst)
    assert lst.delete(90)


def test_lenght():
    lst = LinkedList()
    lst.insert_at_tail(5)
    lst.insert_at_tail(90)
    lst.insert_at_tail(10)
    lst.insert_at_tail(4)

    assert lst.length() == 4
    assert lst.delete(5)
    assert lst.length() == 3


def test_reverse():
    lst = LinkedList()
    lst.insert_at_tail(5)
    lst.insert_at_tail(90)
    lst.insert_at_tail(10)
    lst.insert_at_tail(4)

    lst.reverse()

    assert str(lst) == "4 -> 10 -> 90 -> 5 -> None"

    lst = LinkedList()
    lst.insert_at_tail(10)
    lst.insert_at_tail(9)
    lst.insert_at_tail(4)
    lst.insert_at_tail(6)

    lst.reverse()

    assert str(lst) == "6 -> 4 -> 9 -> 10 -> None"

    lst = LinkedList()
    lst.insert_at_tail(10)

    lst.reverse()

    assert str(lst) == "10 -> None"

    lst = LinkedList()
    lst.reverse()

    assert str(lst) == "None"


def test_detected_loop():
    lst = LinkedList()
    lst.insert_at_tail(5)
    lst.insert_at_tail(90)
    lst.insert_at_tail(10)
    lst.insert_at_tail(4)
    node = lst.search(4)
    other_node = lst.search(90)
    node.next_element = other_node

    assert lst.detect_loop()

    lst = LinkedList()
    lst.insert_at_tail(5)
    lst.insert_at_tail(90)
    lst.insert_at_tail(10)
    lst.insert_at_tail(4)

    assert not lst.detect_loop()