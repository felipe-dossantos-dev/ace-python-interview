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
            return "None"
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
                return current_node
            current_node = current_node.next_element
        return None

    def length(self):
        curr = self.get_head()
        length = 0

        while curr is not None:
            length += 1
            curr = curr.next_element
        return length

    def delete_at_head(self):
        first_element = self.get_head()
        if first_element is not None:
            self.head_node = first_element.next_element
            first_element.next_element = None
        return

    def delete(self, value):
        if self.is_empty():
            return None
        current_node = self.get_head()
        if current_node.data == value:
            self.delete_at_head()
            return current_node
        last_node = current_node
        while current_node:
            if current_node.data == value:
                last_node.next_element = current_node.next_element
                current_node.next_element = None
                return current_node
            last_node = current_node
            current_node = current_node.next_element
        return None

    def reverse(self):
        current_node = self.get_head()
        last_node = None
        while current_node:
            next_node = current_node.next_element

            current_node.next_element = last_node

            last_node = current_node
            current_node = next_node
        self.head_node = last_node

    def search_recursive(self, value):
        return self.__search_recursive(self.get_head(), value)

    def __search_recursive(self, node, value):
        if not node:
            return None
        if node.data is value:
            return node
        return self.__search_recursive(node.next_element, value)
