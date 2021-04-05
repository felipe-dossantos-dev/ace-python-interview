from typing import Mapping

# time O(n^2)
# space O(n^2)
# pythonic / one-liner
def find_max_sum_sublist_pythonic(lst):
    return max(
        [
            sum([lst[k] for k in range(i, j + 1)])
            for i in range(len(lst))
            for j in range(i, len(lst))
        ]
    )


# time O(n^2)
# space O(1)
def find_max_sum_sublist_brute_force(lst):
    max_sum = float("-inf")
    for i in range(len(lst)):
        local_sum = 0
        for j in range(i, len(lst)):
            local_sum += lst[j]
            if local_sum > max_sum:
                max_sum = local_sum
    return max_sum


# theirs solution
# time O(n)
# space O(1)
def find_max_sum_sublist(lst):
    if len(lst) < 1:
        return 0

    curr_max = lst[0]
    global_max = lst[0]
    length_array = len(lst)
    for i in range(1, length_array):
        if curr_max < 0:
            curr_max = lst[i]
        else:
            curr_max += lst[i]
        if global_max < curr_max:
            global_max = curr_max

    return global_max


def test_find_max_sum_sublist():
    assert find_max_sum_sublist([-2, 10, 7, -5, 15, 6]) == 33
    assert find_max_sum_sublist([-4, 2, -5, 1, 2, 3, 6, -5, 1]) == 12
