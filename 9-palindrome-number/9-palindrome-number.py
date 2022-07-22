#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
"""FASTEST SOLUTION

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        
        return str(x) == str(x)[::-1]
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        inputnum = x
        rev = 0
        while x > 0:
            rev = rev * 10 + x % 10
            x = x // 10

        return rev == inputnum


# @lc code=end