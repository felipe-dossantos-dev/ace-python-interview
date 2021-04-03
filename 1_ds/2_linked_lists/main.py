class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None


class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        if self.head_node is None:  # Check whether the head is None
            return True
        else:
            return False

    def insert_at_tail(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head_node = new_node
            return
        temp = self.get_head()
        while temp.next_element is not None:
            temp = temp.next_element
        temp.next_element = new_node

    # Supplementary print function
    def __repr__(self):
        if self.is_empty():
            return ""
        s = ""
        temp = self.head_node
        while temp.next_element is not None:
            s += repr(temp.data) + " -> "
            temp = temp.next_element
        s += repr(temp.data) + " -> None"
        return s


def search(lst, value):
    # Write your code here
    pass


if __name__ == "__main__":
    lst = LinkedList()
    lst.insert_at_tail(0)
    lst.insert_at_tail(1)
    lst.insert_at_tail(2)
    lst.insert_at_tail(3)
