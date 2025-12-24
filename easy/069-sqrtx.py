# LeetCode 69: Sqrt(x)
# -------------------
# Goal:
# Given a non-negative integer x, return the integer part of its square root.
# The result should be rounded down (i.e., floor of the square root).
#
# Approach:
# Use binary search to efficiently find the largest integer m such that m * m <= x.
#
# Why binary search?
# - The square root lies between 0 and x
# - Binary search reduces time complexity to O(log x)

class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0

        while l <= r:
            # Calculate midpoint safely
            m = l + (r - l) // 2

            if m * m > x:
                # Midpoint squared is too large, search left half
                r = m - 1
            elif m * m < x:
                # Midpoint squared is valid, store result and search right half
                res = m
                l = m + 1
            else:
                # Exact square root found
                return m

        return res
