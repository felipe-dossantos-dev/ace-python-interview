def remove_even(list):
    return [x for x in list if abs(x) % 2 == 1 ]

if __name__ == "__main__":
    assert remove_even([1,2,4,5,10,6,3]) == [1,5,3]