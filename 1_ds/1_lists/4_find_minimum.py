# time - O(n)
def find_minimum(arr):
    return min(arr)

# theirs solution
# O(n log n)
def find_minimum_sort(lst):
    if (len(lst) <= 0):
        return None
    lst.sort()  # sort list
    return lst[0]  # return first element

if __name__ == "__main__":
    assert find_minimum([9,2,3,6]) == 2