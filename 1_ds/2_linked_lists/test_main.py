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


def test_find_mid():
    lst = LinkedList()
    lst.insert_at_tail(5)
    lst.insert_at_tail(90)
    lst.insert_at_tail(10)
    lst.insert_at_tail(4)

    assert lst.find_mid().data == 90

    lst.insert_at_tail(0)
    assert lst.find_mid().data == 10


def test_remove_duplicates():
    lst = LinkedList()
    lst.insert_at_tail(5)
    lst.insert_at_tail(90)
    lst.insert_at_tail(10)
    lst.insert_at_tail(4)
    lst.remove_duplicates()

    assert str(lst) == "5 -> 90 -> 10 -> 4 -> None"

    lst = LinkedList()
    lst.insert_at_tail(1)
    lst.insert_at_tail(2)
    lst.insert_at_tail(2)
    lst.insert_at_tail(2)
    lst.insert_at_tail(3)
    lst.insert_at_tail(4)
    lst.insert_at_tail(4)
    lst.insert_at_tail(5)
    lst.insert_at_tail(6)
    lst.remove_duplicates()

    assert str(lst) == "1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None"

    lst = LinkedList()
    lst.insert_at_tail(90)
    lst.insert_at_tail(90)
    lst.insert_at_tail(10)
    lst.insert_at_tail(10)
    lst.insert_at_tail(10)
    lst.insert_at_tail(4)
    lst.insert_at_tail(4)
    lst.insert_at_tail(4)
    lst.remove_duplicates()

    assert str(lst) == "90 -> 10 -> 4 -> None"


def test_union():
    lst = LinkedList()
    lst.insert_at_tail(5)
    lst.insert_at_tail(90)
    lst.insert_at_tail(10)
    lst.insert_at_tail(4)

    lst2 = LinkedList()
    lst2.insert_at_tail(1)
    lst2.insert_at_tail(2)
    lst2.insert_at_tail(2)
    lst2.insert_at_tail(2)
    lst2.insert_at_tail(3)
    lst2.insert_at_tail(4)
    lst2.insert_at_tail(4)
    lst2.insert_at_tail(5)
    lst2.insert_at_tail(6)

    lst = lst.union(lst2)
    assert str(lst) == "5 -> 90 -> 10 -> 4 -> 1 -> 2 -> 3 -> 6 -> None"

    lst = LinkedList()
    lst.insert_at_tail(10)
    lst.insert_at_tail(20)
    lst.insert_at_tail(80)
    lst.insert_at_tail(60)

    lst2 = LinkedList()
    lst2.insert_at_tail(15)
    lst2.insert_at_tail(20)
    lst2.insert_at_tail(30)
    lst2.insert_at_tail(60)
    lst2.insert_at_tail(45)

    lst = lst.union(lst2)
    assert str(lst) == "10 -> 20 -> 80 -> 60 -> 15 -> 30 -> 45 -> None"


def test_intersection():
    lst = LinkedList()
    lst.insert_at_tail(5)
    lst.insert_at_tail(90)
    lst.insert_at_tail(10)
    lst.insert_at_tail(4)

    lst2 = LinkedList()
    lst2.insert_at_tail(1)
    lst2.insert_at_tail(2)
    lst2.insert_at_tail(2)
    lst2.insert_at_tail(2)
    lst2.insert_at_tail(3)
    lst2.insert_at_tail(4)
    lst2.insert_at_tail(4)
    lst2.insert_at_tail(5)
    lst2.insert_at_tail(6)

    lst = lst.intersection(lst2)
    assert str(lst) == "5 -> 4 -> None"

    lst = LinkedList()
    lst.insert_at_tail(10)
    lst.insert_at_tail(20)
    lst.insert_at_tail(80)
    lst.insert_at_tail(60)

    lst2 = LinkedList()
    lst2.insert_at_tail(15)
    lst2.insert_at_tail(20)
    lst2.insert_at_tail(30)
    lst2.insert_at_tail(60)
    lst2.insert_at_tail(45)

    lst = lst.intersection(lst2)
    assert str(lst) == "20 -> 60 -> None"


def test_find_nth():
    lst = LinkedList()
    lst.insert_at_tail(5)
    lst.insert_at_tail(90)
    lst.insert_at_tail(10)
    lst.insert_at_tail(4)

    assert lst.find_nth(2) == 10

    lst = LinkedList()
    lst.insert_at_tail(15)
    lst.insert_at_tail(22)
    lst.insert_at_tail(8)
    lst.insert_at_tail(7)
    lst.insert_at_tail(14)
    lst.insert_at_tail(21)
    assert lst.find_nth(4) == 8
    assert lst.find_nth(5) == 22
    assert lst.find_nth(8) == -1
    assert lst.find_nth(2) == 14


def test_reverse_every_k_elements():
    lst = LinkedList()
    lst.insert_at_tail(5)
    lst.insert_at_tail(90)
    lst.insert_at_tail(10)
    lst.insert_at_tail(4)
    lst.reverse_every_k_elements(4)
    assert str(lst) == "4 -> 10 -> 90 -> 5 -> None"

    lst = LinkedList()
    lst.insert_at_tail(5)
    lst.insert_at_tail(90)
    lst.insert_at_tail(10)
    lst.insert_at_tail(4)
    lst.reverse_every_k_elements(2)
    assert str(lst) == "90 -> 5 -> 4 -> 10 -> None"

    lst2 = LinkedList()
    lst2.insert_at_tail(1)
    lst2.insert_at_tail(2)
    lst2.insert_at_tail(3)
    lst2.insert_at_tail(4)
    lst2.insert_at_tail(5)
    lst2.insert_at_tail(6)
    lst2.insert_at_tail(7)
    lst2.insert_at_tail(8)
    lst2.insert_at_tail(9)
    lst2.reverse_every_k_elements(3)
    assert str(lst2) == "3 -> 2 -> 1 -> 6 -> 5 -> 4 -> 9 -> 8 -> 7 -> None"