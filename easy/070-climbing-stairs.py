# LeetCode 70: Climbing Stairs
# ---------------------------
# Goal:
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps.
# Return the total number of distinct ways to reach the top.
#
# Approach:
# This is a classic Dynamic Programming problem.
# The number of ways to reach step n is:
#   ways(n) = ways(n - 1) + ways(n - 2)
#
# Optimization:
# Instead of using an array, keep only the last two values
# to achieve O(1) space complexity.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases:
        # one -> ways to reach current step
        # two -> ways to reach previous step
        one, two = 1, 1

        # Iterate n - 1 times to build up the solution
        for _ in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one
