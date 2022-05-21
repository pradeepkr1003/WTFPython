"""
Two Steps:
    1. Figure out the base case
    2. Divide the problem until it becomes the base case.
"""
from typing import List


# [Working]
def sum_list(list_: List[int], list_sum_: int = 0) -> int:
    # sum of list with divide and concure method
    while list_.__len__():
        list_sum_ += list_.pop()
    return list_sum_



# [Not Working]
def _sum_list(list_: List[int], list_sum_: int = 0) -> int:
    # sum of list with divide and concure method
    if list_:
        list_sum_ += list_.pop()
        _sum_list(list_, list_sum_)
        # return _sum_list(list_, list_sum_)
    return list_sum_


# StdIn:
_num_list = [1, 2]

# Stdout
print('stdout: [from first function] ', sum_list(_num_list))
print('stdout: [from second function] ', _sum_list(_num_list))
