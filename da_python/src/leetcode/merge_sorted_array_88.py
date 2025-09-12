# Problem: 88. Merge Sorted Array
# URL: https://leetcode.com/problems/merge-sorted-array/
#
# You are given two integer arrays a and b, sorted in non-decreasing order, and two integers m and n, representing the number of elements in a and b respectively.
#
# Merge a and b into a single array sorted in non-decreasing order.
#
# The final sorted array should not be returned by the function, but instead be stored inside the array a. To accommodate this, a has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. b has a length of n.
#
# Constraints:
# a.length == m + n
# b.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -10^9 <= a[i], b[j] <= 10^9


def merge(a: list[int], m: int, b: list[int], n: int) -> None:
    """
    Do not return anything, modify a in-place instead.
    """
    a_idx = m - 1
    b_idx = n - 1
    w_idx = m + n - 1

    while b_idx >= 0:
        if a_idx >= 0 and a[a_idx] > b[b_idx]:
            a[w_idx] = a[a_idx]
            a_idx -= 1
        else:
            a[w_idx] = b[b_idx]
            b_idx -= 1
        w_idx -= 1
