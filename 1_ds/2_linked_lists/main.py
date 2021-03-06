from typing import AsyncContextManager


class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None
        self.arbitrary_pointer = None


class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        return self.head_node is None  # Check whether the head is None

    def insert_at_tail(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head_node = new_node
            return new_node
        temp = self.get_head()
        while temp.next_element is not None:
            temp = temp.next_element
        temp.next_element = new_node
        return new_node

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

    def reverse_every_k_elements(self, k):
        if k < 2:
            return

        current, previous = self.get_head(), None
        while True:

            last_node_previous_list = previous
            last_node_current_list = current

            next_node = None
            i = 0
            while current is not None and i < k:
                next_node = current.next_element
                current.next_element = previous
                previous = current
                current = next_node
                i += 1

            if last_node_previous_list is not None:
                last_node_previous_list.next_element = previous
            else:
                self.head_node = previous

            last_node_current_list.next_element = current

            if current is None:
                break
            previous = last_node_current_list

    # time O(2n) -> O(n)
    # space O(1)
    def rotate(self, k):
        if k == 0:
            return

        leng = self.length()
        rotate = leng - abs(k % leng)
        if rotate == 0:
            return

        node = self.get_head()
        previous = None
        while rotate:
            previous = node
            node = node.next_element
            rotate -= 1

        last_head = self.get_head()
        self.head_node = node
        previous.next_element = None

        # ok
        last = None
        while node:
            last = node
            node = node.next_element
        last.next_element = last_head

    def add_integer(self, another_list):
        """
        Description: Given the head pointers of two linked lists where each linked list represents an integer number (each node is a digit),
        add them and return the resulting linked list. Here, the first node in a list represents the least significant digit.
        Solution:
            space O(n)
            time O(n)
        In some cases, the interviewer might ask that digits in the linked list are stored from left to right, i.e., the most significant digit comes first. We have two options in this case:
          - Reverse the input linked lists and apply the above algorithm.
          - If we have circular doubly linked lists, we can simply run the above algorithm from tail to head and keep adding the resulting digit at the head of the result linked list.
        Follow-up questions
        How would we multiply two large numbers?
        How would we divide two large integers?
        What if the numbers are not in base 10, for instance, base 2, 5, or 8?
        """
        lst = LinkedList()
        cur_head = self.get_head()
        another_head = another_list.get_head()
        upper = 0
        while cur_head or another_head or upper > 0:
            cur_head_value = cur_head.data if cur_head else 0
            another_head_value = another_head.data if another_head else 0

            actual = cur_head_value + another_head_value + upper
            upper = actual // 10
            actual = actual % 10

            lst.insert_at_tail(actual)
            if cur_head:
                cur_head = cur_head.next_element
            if another_head:
                another_head = another_head.next_element

        return lst

    def deep_copy_arbitrary_pointer(self):
        """
        We are given a linked list where the node has two pointers.
        The first is the regular next pointer.
        The second pointer is called arbitrary_pointer and it can point to any node in the linked list.
        Your job is to write code to make a deep copy of the given linked list.
        Here, deep copy means that any operations on the original list (inserting, modifying and removing) should not affect the copied list.
        """
        lst = LinkedList()
        mapping = {}

        cur_head = self.get_head()
        while cur_head:
            node = lst.insert_at_tail(cur_head.data)
            mapping[cur_head] = node
            cur_head = cur_head.next_element

        cur_head = self.get_head()
        while cur_head:
            node = mapping[cur_head]
            if node and cur_head.arbitrary_pointer:
                arb_node = mapping[cur_head.arbitrary_pointer]
                node.arbitrary_pointer = arb_node
            cur_head = cur_head.next_element

        return lst
