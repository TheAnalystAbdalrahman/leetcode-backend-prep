# LeetCode 217: Contains Duplicate
# --------------------------------
# Goal:
# Given an integer array nums, return True if any value appears
# at least twice in the array, and False if every element is distinct.
#
# Approach:
# Use a set to remove duplicates.
# - A set stores only unique values
# - If the length of the set is smaller than the list,
#   then duplicates exist
#
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Compare number of unique elements to total elements
        if len(set(nums)) == len(nums):
            return False
        else:
            return True
