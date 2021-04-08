# time O(m + n)
def intersect(head1, head2):
    a_head1 = head1
    c_head1 = 0
    while a_head1:
        c_head1 += 1
        a_head1 = a_head1.next

    a_head2 = head2
    c_head2 = 0
    while a_head2:
        c_head2 += 1
        a_head2 = a_head2.next

    max_head = None
    min_head = None
    diff = abs(c_head1 - c_head2)
    if c_head1 >= c_head2:
        min_head = head2
        max_head = head1
    else:
        min_head = head1
        max_head = head2

    for i in range(diff):
        max_head = max_head.next
    while max_head:
        if max_head == min_head:
            return max_head
        max_head = max_head.next
        min_head = min_head.next
    return None