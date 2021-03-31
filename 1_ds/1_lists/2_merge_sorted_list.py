# my solution - creating new list
# time O(n + m)
# space O(n + m)
def merge_lists(lst1, lst2):
    new_list = []
    c1, c2 = 0, 0
    l1, l2 = len(lst1), len(lst2)
    total = l1 + l2
    while c1 + c2 < total:
        if c1 >= l1:
            new_list.append(lst2[c2])
            c2 += 1
        elif c2 >= l2:
            new_list.append(lst1[c1])
            c1 += 1
        elif lst1[c1] < lst2[c2]:
            new_list.append(lst1[c1])
            c1 += 1
        else:
            new_list.append(lst2[c2])
            c2 += 1
    return new_list


# their solution - merging in place
# medium case => time O(m(n+m)) space O(m)
# if m > n, we have O(mn)
# elif n > m O(n^2)
# However, the extra space used in solution#1 is reduced to O(m) in solution#2.
# Thus, it makes this a tradeoff between space and time.
def merge_lists_in_place(lst1, lst2):
    ind1 = 0  # Creating 2 new variable to track the 'current index'
    ind2 = 0
    # While both indeces are less than the length of their lists
    while ind1 < len(lst1) and ind2 < len(lst2):
        # If the current element of list1 is greater
        # than the current element of list2
        if lst1[ind1] > lst2[ind2]:
            # insert list2's current index to list1
            lst1.insert(ind1, lst2[ind2])
            ind1 += 1  # increment indices
            ind2 += 1
        else:
            ind1 += 1

    if ind2 < len(lst2):  # Append whatever is left of list2 to list1
        lst1.extend(lst2[ind2:])
    return lst1


if __name__ == "__main__":
    assert merge_lists([1, 3], [6, 7]) == [1, 3, 6, 7]
    assert merge_lists([6, 7], [1, 3]) == [1, 3, 6, 7]
    assert merge_lists([1, 3, 4, 5], [2, 6, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert merge_lists([1, 2, 3, 5, 7], [1, 2, 3, 5, 7]) == [
        1,
        1,
        2,
        2,
        3,
        3,
        5,
        5,
        7,
        7,
    ]
