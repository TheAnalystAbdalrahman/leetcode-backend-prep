# LeetCode 448: Find All Numbers Disappeared in an Array
# ----------------------------------------------------
# Goal:
# Given an array nums of length n where each number is in the range [1, n],
# return all the numbers in the range [1, n] that do not appear in nums.
#
# Approach:
# Use the input array itself to mark which numbers are present.
#
# Key idea:
# - Each value v in nums corresponds to index v - 1
# - Mark presence by making nums[v - 1] negative
# - After marking, indices that remain positive correspond to missing numbers
#
# This works because:
# - All values are guaranteed to be within [1, n]
# - We are allowed to modify the input array
#
# Time Complexity: O(n)
# Space Complexity: O(1) (excluding output list)

from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Step 1: Mark presence of each number
        for n in nums:
            i = abs(n) - 1
            nums[i] = -abs(nums[i])

        res = []

        # Step 2: Collect indices that were never marked
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)

        return res
