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

    def search(self, value):
        current_node = self.get_head()
        while current_node:
            if current_node.data == value:
                return True
            current_node = current_node.next_element
        return False

    def search_recursive(self, value):
        return self.__search_recursive(self.get_head(), value)

    def __search_recursive(self, node, value):
        if not node:
            return False
        if node.data is value:
            return True
        return self.__search_recursive(node.next_element, value)


if __name__ == "__main__":
    assert True
