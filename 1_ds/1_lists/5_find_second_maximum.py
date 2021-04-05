# time O(n)
def find_second_maximum(lst):
    max_value = float("-inf")
    second_value = float("-inf")
    # quebra no caso de ter dois iguais
    for i in lst:
        if i > max_value:
            second_value = max_value
            max_value = i
        elif i > second_value and i != max_value:
            second_value = i
    return second_value


# theirs solution
# time O(nlogn)
def find_second_maximum_sort(lst):
    lst.sort()
    if len(lst) >= 2:
        return lst[-2]
    else:
        return None


# time O(2n) -> O(n)
def find_second_maximum_two_traverse(lst):
    first_max = float("-inf")
    second_max = float("-inf")
    # find first max
    for item in lst:
        if item > first_max:
            first_max = item
    # find max relative to first max
    for item in lst:
        if item != first_max and item > second_max:
            second_max = item
    return second_max


# time O(n)
def find_second_maximum_one_traverse(lst):
    if len(lst) < 2:
        return
    # initialize the two to infinity
    max_no = second_max_no = float("-inf")
    for i in range(len(lst)):
        # update the max_no if max_no value found
        if lst[i] > max_no:
            second_max_no = max_no
            max_no = lst[i]
        # check if it is the second_max_no and not equal to max_no
        elif lst[i] > second_max_no and lst[i] != max_no:
            second_max_no = lst[i]
    if second_max_no == float("-inf"):
        return
    else:
        return second_max_no


def test_find_second_maximum():
    assert find_second_maximum([9, 2, 3, 6]) == 6
    assert find_second_maximum([9, 9, 8, 5, 0]) == 8
    assert find_second_maximum([4, 2, 1, 5, 0]) == 4
