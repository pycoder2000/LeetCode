#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start

# BEST SOLUTION
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         translations = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000
#         }
#         number = 0
#         s = s.replace("IV", "IIII").replace("IX", "VIIII")
#         s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
#         s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
#         for char in s:
#             number += translations[char]
#         return number


# ANOTHER GOOD SOLUTION
# def romanToInt(self, s):
#     roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     previous, total = 0, 0
#     for char in s:
#         current = roman[char]
#         total += current
#         # need to subtract
#         if current > previous:
#             total -= 2 * previous
#         previous = current
#     return total


# MY SOLUTION
class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        i = 0
        while i < len(s):
            if s[i] == "I":
                if (i + 1) < len(s) and s[i + 1] == "V":
                    i = i + 2
                    result += 4
                elif (i + 1) < len(s) and s[i + 1] == "X":
                    i = i + 2
                    result += 9
                else:
                    i = i + 1
                    result += 1
            elif s[i] == "X":
                if (i + 1) < len(s) and s[i + 1] == "L":
                    i = i + 2
                    result += 40
                elif (i + 1) < len(s) and s[i + 1] == "C":
                    i = i + 2
                    result += 90
                else:
                    i = i + 1
                    result += 10
            elif s[i] == "C":
                if (i + 1) < len(s) and s[i + 1] == "D":
                    i = i + 2
                    result += 400
                elif (i + 1) < len(s) and s[i + 1] == "M":
                    i = i + 2
                    result += 900
                else:
                    i = i + 1
                    result += 100
            elif s[i] == "V":
                i = i + 1
                result += 5
            elif s[i] == "L":
                i = i + 1
                result += 50
            elif s[i] == "D":
                i = i + 1
                result += 500
            elif s[i] == "M":
                i = i + 1
                result += 1000
        return result


# @lc code=end
