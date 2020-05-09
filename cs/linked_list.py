class LinkedList:

    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

        def __str__(self):
            return f'{self.data}'

        def is_empty(self):
            return self.data is None

    def __init__(self, data=None):
        if data is None:
            self.head = None
        else:
            self.head = LinkedList.Node(data)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node.data
            node = node.next

    def __bool__(self):
        return self.is_empty()

    def __str__(self):
        return " -> ".join(map(str, self))

    @classmethod
    def from_iter(cls, iterable):
        new_list = LinkedList()

        for item in reversed(iterable):
            new_list.insert_beginning(item)

        return new_list

    def insert_beginning(self, new_data):
        new_node = LinkedList.Node(new_data, self.head)
        self.head = new_node

    def insert_after(self, node, new_data):
        new_node = LinkedList.Node(new_data, node.next)
        node.next = new_node

    def reverse(self):
        curr = self.head
        prev = next = None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        self.head = prev

    def is_empty(self):
        return self.head is None or self.head.is_empty()
