import itertools

# pythonic challenge / one liner
def max_min(lst):
    return list(
        itertools.chain.from_iterable(
            [[lst[-(i + 1)], lst[i]] for i in range(len(lst) // 2)]
            + ([] if len(lst) % 2 == 0 else [[lst[len(lst) // 2]]])
        )
    )


# time O(n)
# space O(n)
def max_min_basic(lst):
    min_index = 0
    max_index = 1
    new_list = []
    while min_index + max_index <= len(lst):
        if (max_index + min_index) % 2 == 1:
            new_list.append(lst[len(lst) - max_index])
            max_index += 1
        else:
            new_list.append(lst[min_index])
            min_index += 1
    return new_list


# theirs solution
# time O(n)
# space O(n)
def max_min_new_list(lst):
    result = []
    # iterate half list
    for i in range(len(lst) // 2):
        # Append corresponding last element
        result.append(lst[-(i + 1)])
        # append current element
        result.append(lst[i])
    if len(lst) % 2 == 1:
        # if middle value then append
        result.append(lst[len(lst) // 2])
    return result


# time O(2n) -> O(n)
# space O(1)
def max_min_no_extra_space(lst):
    # Return empty list for empty list
    if len(lst) == 0:
        return []

    maxIdx = len(lst) - 1  # max index
    minIdx = 0  # first index
    maxElem = lst[-1] + 1  # Max element
    # traverse the list
    for i in range(len(lst)):
        # even number means max element to append
        if i % 2 == 0:
            lst[i] += (lst[maxIdx] % maxElem) * maxElem
            maxIdx -= 1
        # odd number means min number
        else:
            lst[i] += (lst[minIdx] % maxElem) * maxElem
            minIdx += 1

    for i in range(len(lst)):
        lst[i] = lst[i] // maxElem
    return lst


def test_max_min():
    assert max_min([1, 2, 3, 4, 5]) == [5, 1, 4, 2, 3]
    assert max_min([1, 2, 3, 4, 5, 6, 7]) == [7, 1, 6, 2, 5, 3, 4]
