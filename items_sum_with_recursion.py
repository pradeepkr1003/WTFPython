"""
Two Steps:
    1. Figure out the base case
    2. Divide the problem until it becomes the base case.
"""
import timeit
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
        # _sum_list(list_, list_sum_)
        return _sum_list(list_, list_sum_)
    return list_sum_


# > -- [Find the Max Value in a list]

def find_max(_list_: List[int], max_: int = 0) -> int:
    val = _list_.pop()

    if _list_:
        if val > max_:
            max_ = val

        return find_max(_list_, max_)

    else:
        return max_


def qsort(_list_: List[int]) -> int:
    # Quick Sort
    if _list_.__len__() < 2:
        return _list_

    else:
        pivot = _list_[0]

        smaller = [x for x in _list_[1:] if x <= pivot]
        greater = [x for x in _list_[1:] if x >= pivot]

        return qsort(smaller) + [pivot] + qsort(greater)


def qsort_faster(_list_: List[int]) -> int:
    # Quick Sort a bit faster
    if _list_.__len__() < 2:
        return _list_

    else:
        len_ = len(_list_) // 2
        pivot = _list_[len_]

        smaller = [x for x in _list_[1:] if x <= pivot]
        greater = [x for x in _list_[1:] if x >= pivot]

        return qsort(smaller) + [pivot] + qsort(greater)


# StdIn:
# ======
_num_list = [1, 2, 3]

# Stdout
# ======


# print('stdout: [from first function] ', sum_list(_num_list))
# print('stdout: [from second function] ', _sum_list(_num_list))

# -
print('MAX (func) :', find_max(_num_list))
# -


# print('qsort with middle pivot', timeit.repeat(
#     'qsort_faster([x for x in range(500)])', 'from __main__ import qsort_faster', number=1))

# -

# print('qsort with starting value as pivot', timeit.repeat(
#     'qsort([x for x in range(950)])', 'from __main__ import qsort', number=1))

# qsort(_num_list)
