#
# @lc app=leetcode id=1208 lang=python3
#
# [1208] Get Equal Substrings Within Budget
#

# @lc code=start
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        diff = [abs(ord(c1) - ord(c2)) for c1, c2 in zip(s, t)]
        left = total = ans = 0
        for right in range(len(t)):
            total += diff[right]
            while total > maxCost:
                total -= diff[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans
# @lc code=end

