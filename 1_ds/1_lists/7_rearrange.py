# time O(n)
# space O(n)
def rearrange(lst):
    neg_list = []
    pos_list = []
    for i in lst:
        if i >= 0:
            pos_list.append(i)
        else:
            neg_list.append(i)
    return neg_list + pos_list


# theirs solution
# time O(n)
# space O(1)
def rearrange_inplace(lst):
    leftMostPosEle = 0  # index of left most element
    # iterate the list
    for curr in range(len(lst)):
        # if negative number
        if lst[curr] < 0:
            # if not the last negative number
            if curr is not leftMostPosEle:
                # swap the two
                lst[curr], lst[leftMostPosEle] = lst[leftMostPosEle], lst[curr]
            # update the last position
            leftMostPosEle += 1
    return lst


# time O(n)
# space O(n)
def rearrange_pythonic(lst):
    # get negative and positive list after filter and then merge
    return [i for i in lst if i < 0] + [i for i in lst if i >= 0]


def test_rearrange():
    assert rearrange([10, -1, 20, 4, 5, -9, -6]) == [-1, -9, -6, 10, 20, 4, 5]
    assert rearrange([0, 0, 0, -2]) == [-2, 0, 0, 0]
    assert rearrange([300, -1, 3, 0]) == [-1, 300, 3, 0]
