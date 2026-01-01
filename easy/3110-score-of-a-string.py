# LeetCode 3110: Score of a String
# -------------------------------
# Goal:
# Given a string s, calculate its score by summing the absolute
# differences between the ASCII values of consecutive characters.
#
# Approach:
# - Iterate through the string from index 0 to len(s) - 2
# - For each adjacent pair of characters:
#     * Convert characters to ASCII using ord()
#     * Add the absolute difference to the result
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0

        # Iterate over adjacent character pairs
        for i in range(len(s) - 1):
            res += abs(ord(s[i]) - ord(s[i + 1]))

        return res
