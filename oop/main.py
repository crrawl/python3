#!/usr/bin/env python3
# PATH=$PATH:/mnt/c/python3/tmpscirpt


arr = [0, 1, 2, 3, 3]


def odd_or_even(arr):
    return 'odd' if sum(arr) % 2 else 'even'
    # arr_sum = 0
    # for i in arr:
    #     arr_sum += i

    # if arr_sum % 2 == 0:
    #     return 'even'
    # else:
    #     return 'odd'

print(odd_or_even(arr))
