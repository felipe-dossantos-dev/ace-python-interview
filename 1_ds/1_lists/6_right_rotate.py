# time O(kn)
# space O(1)
def right_rotate(lst, k):
    leng = len(lst)
    for _ in range(k):
        for i in range(leng - 1, 0, -1):
            new_index = abs(i - 1) % leng
            lst[i], lst[new_index] = lst[new_index], lst[i]
    return lst


# time O(n)
# space O(n)
def right_rotate_basic(lst, k):
    leng = len(lst)
    new_list = [0] * leng
    for n, i in enumerate(lst):
        new_index = (n + k) % leng
        new_list[new_index] = i
    return new_list


# theirs solution
# time O(n)
# space O(n)
def right_rotate_manual(lst, k):
    k = 0 if len(lst) == 0 else k % len(lst)
    rotatedList = []
    # get the elements from the end
    for item in range(len(lst) - k, len(lst)):
        rotatedList.append(lst[item])
    # get the remaining elements
    for item in range(0, len(lst) - k):
        rotatedList.append(lst[item])
    return rotatedList


# pythonic
# time O(n)
# space O(n)
def right_rotate_pythonic(lst, k):
    # get rotation index
    k = 0 if len(lst) == 0 else k % len(lst)
    return lst[-k:] + lst[:-k]


if __name__ == "__main__":
    assert right_rotate([10, 20, 30, 40, 50], 3) == [30, 40, 50, 10, 20]
    assert right_rotate([10, 20, 30, 40, 50], 0) == [10, 20, 30, 40, 50]
