from linked_list import LinkedList


def test_init_list():
    ll1 = LinkedList()
    assert ll1.is_empty()

    ll2 = LinkedList(0)
    assert not ll2.is_empty()


def test_init_from_iterable():
    ll1 = LinkedList.from_iter([1, 2, 3])
    assert not ll1.is_empty()


def test_to_str():
    ll1 = LinkedList.from_iter([1, 2, 3])
    assert str(ll1) == '3 -> 2 -> 1'


def test_iter():
    ll1 = LinkedList.from_iter([1, 2, 3])
    assert [item for item in ll1] == [3, 2, 1]


def test_insert_after():
    ll1 = LinkedList(1)
    ll1.insert_after(ll1.head, 2)
    ll1.insert_after(ll1.head, 3)
    assert [item for item in ll1] == [1, 3, 2]


if __name__ == '__main__':
    test_init_list()
    test_init_from_iterable()
    test_to_str()
    test_iter()
    print("Test LinkedList :: OK")
