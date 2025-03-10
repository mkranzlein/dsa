"""Implementations of sorting algorithms for arrays/lists."""
from math import ceil


def merge(a: list[int], b: list[int]) -> list[int]:
    """Merge two sorted lists."""
    i = 0
    j = 0
    result = []
    while (i < len(a)) or (j < len(b)):
        # Check if a has elements remaining
        if i < len(a):
            # If b is exhausted, add next element of a
            if j == len(b):
                result.append(a[i])
                i += 1
            # Otherwise, compare next elements of a and b
            else:
                if a[i] < b[j]:
                    result.append(a[i])
                    i += 1
                else:
                    result.append(b[j])
                    j += 1
        else:
            result.append(b[j])
            j += 1
    return result


def merge_sort(x: list[int]) -> list[int]:
    """Sort list of ints in non-decreasing order."""
    # Base cases
    if len(x) == 0 or len(x) == 1:
        return x

    if len(x) == 2:
        if x[0] > x[1]:
            return [x[1], x[0]]
        else:
            return x

    # Recursive case
    halfway = ceil(len(x) / 2)
    left_half = x[:halfway]
    right_half = x[halfway:]
    return merge(merge_sort(left_half), merge_sort(right_half))
