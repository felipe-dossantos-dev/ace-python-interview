# time O(n)
# space O(n)
def find_happy_number(num):
    passed_numbers = set()
    while num != 1 and num not in passed_numbers:
        total = 0
        sum_num = num
        while sum_num:
            total += (sum_num % 10) ** 2
            sum_num = sum_num // 10
        passed_numbers.add(num)
        num = total
    return num == 1


# theirs solution
# time O(log N)
# space O(1)
def find_happy_number_theirs(num):
    slow, fast = num, num
    while True:
        slow = find_square_sum(slow)  # move one step
        fast = find_square_sum(find_square_sum(fast))  # move two steps
        if slow == fast:  # found the cycle
            break
    return slow == 1  # see if the cycle is stuck on the number '1'


def find_square_sum(num):
    _sum = 0
    while num > 0:
        digit = num % 10
        _sum += digit * digit
        num //= 10
    return _sum


def test_find_happy_number():
    assert find_happy_number(23)
    assert not find_happy_number(12)