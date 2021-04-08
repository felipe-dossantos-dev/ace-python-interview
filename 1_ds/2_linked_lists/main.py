from typing import AsyncContextManager


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

    # time average O(n), worst case O(n^2) because set lookup can take O(n)
    def detect_loop(self):
        nodes_passed = set()
        curr = self.get_head()
        while curr is not None:
            if curr in nodes_passed:
                return True
            nodes_passed.add(curr)
            curr = curr.next_element
        return False

    # Floyd's Cycle Finding Algorithm
    # time O(n)
    def detect_loop_2(self):
        # Keep two iterators
        onestep = self.get_head()
        twostep = self.get_head()
        while onestep and twostep and twostep.next_element:
            onestep = onestep.next_element  # Moves one node at a time
            twostep = twostep.next_element.next_element  # Skips a node
            if onestep == twostep:  # Loop exists
                return True
        return False

    def find_mid(self):
        leng = self.length()
        mid = leng // 2 + leng % 2
        curr = self.get_head()
        for _ in range(mid - 1):
            curr = curr.next_element
        return curr

    def find_mid_one_pass(self):
        if self.is_empty():
            return -1
        current_node = self.get_head()
        if current_node.next_element == None:
            # Only 1 element exist in array so return its value.
            return current_node.data

        mid_node = current_node
        current_node = current_node.next_element.next_element
        # Move mid_node (Slower) one step at a time
        # Move current_node (Faster) two steps at a time
        # When current_node reaches at end, mid_node will be at the middle of List
        while current_node:
            mid_node = mid_node.next_element
            current_node = current_node.next_element
            if current_node:
                current_node = current_node.next_element
        if mid_node:
            return mid_node.data
        return -1

    # time O(n) on average, O(n^2) on worst case
    # space O(n) for the set
    def remove_duplicates(self):
        nodes_passed = set()
        previous = self.get_head()
        curr = self.get_head()

        while curr:
            if curr.data in nodes_passed:
                previous.next_element = curr.next_element
            else:
                nodes_passed.add(curr.data)
                previous = curr
            curr = curr.next_element

    # time O(n^2)
    def remove_duplicates_theirs(self):
        if self.is_empty():
            return None

        if self.get_head().next_element is None:
            return self

        outer_node = self.get_head()
        while outer_node:
            inner_node = outer_node  # Iterator for the inner loop
            while inner_node:
                if inner_node.next_element:
                    if outer_node.data == inner_node.next_element.data:
                        # Duplicate found, so now removing it
                        new_next_element = inner_node.next_element.next_element
                        inner_node.next_element = new_next_element
                    else:
                        # Otherwise simply iterate ahead
                        inner_node = inner_node.next_element
                else:
                    # Otherwise simply iterate ahead
                    inner_node = inner_node.next_element
            outer_node = outer_node.next_element

        return self

    # TODO - create new list
    # time - O((m + n)^2) worst case because of remove_duplicates worst case
    # time - O(m + n) average case
    # space - O(1)
    def union(self, another_list):
        another_curr = another_list.get_head()
        curr = self.get_head()
        last = None
        while curr:
            last = curr
            curr = curr.next_element
        last.next_element = another_curr
        self.remove_duplicates()
        return self

    # time - O((m + n)^2) worst case
    # time - O(m + n) average case
    # space - O(m + n)
    def intersection(self, another_list):
        another_curr = another_list.get_head()
        curr = self.get_head()
        new_list = LinkedList()
        nodes_passed = set()

        while another_curr:
            nodes_passed.add(another_curr.data)
            another_curr = another_curr.next_element
        while curr:
            if curr.data in nodes_passed:
                new_list.insert_at_tail(curr.data)
            curr = curr.next_element
        return new_list

    # space O(2*n) -> O(n)
    def find_nth(self, n):
        if self.is_empty():
            return -1
        leng = self.length() - n
        if leng <= 0:
            return -1
        cur = self.get_head()
        for i in range(leng):
            cur = cur.next_element
        return cur.data

    # space O(n)
    def find_nth_two_pointers(self, n):
        if self.is_empty():
            return -1

        nth_node = self.get_head()  # This iterator will reach the Nth node
        end_node = self.get_head()  # This iterator will reach the end of the list

        count = 0
        while count < n:
            if end_node is None:
                return -1
            end_node = end_node.next_element
            count += 1

        while end_node is not None:
            end_node = end_node.next_element
            nth_node = nth_node.next_element

        return nth_node.data