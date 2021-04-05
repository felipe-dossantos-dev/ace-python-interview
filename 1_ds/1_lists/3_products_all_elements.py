# my solution
# time O(2*n) -> O(n)
# space O(n)
def find_product(lst):
    total = 1
    has_zero = False
    for i in lst:
        if i != 0:
            total *= i
        else:
            has_zero = True
    new_list = []
    for i in lst:
        value = 0
        if not has_zero:
            value = total / i
        elif has_zero and i == 0:
            value = total
        new_list.append(value)
    return new_list


# theirs solution
# time O(n^2)
# space O(n)
def find_product_nested_loop(lst):
    result = []
    left = 1  # To store product of all previous values from currentIndex
    for i in range(len(lst)):
        currentproduct = 1  # To store current product for index i
        # compute product of values to the right of i index of list
        for ele in lst[i + 1 :]:
            currentproduct = currentproduct * ele
        # currentproduct * product of all values to the left of i index
        result.append(currentproduct * left)
        # Updating `left`
        left = left * lst[i]

    return result


# time O(2*n) -> O(n)
# space O(2*n) -> O(n)
def find_product_optimized(lst):
    # get product start from left
    left = 1
    product = []
    for ele in lst:
        product.append(left)
        left = left * ele
    # get product starting from right
    right = 1
    for i in range(len(lst) - 1, -1, -1):
        product[i] = product[i] * right
        right = right * lst[i]

    return product


def test_find_product():
    assert find_product([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert find_product([4, 2, 1, 5, 0]) == [0, 0, 0, 0, 40]
    assert find_product([2, 5, 9, 3, 6]) == [810, 324, 180, 540, 270]
