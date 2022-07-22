#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonPrefix = ""
        if len(strs) == 0:
            return commonPrefix
        if len(strs) == 1:
            return strs[0]
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return commonPrefix
            commonPrefix += strs[0][i]
        return commonPrefix


# @lc code=end
