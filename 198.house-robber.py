#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = prev1 = 0
        for num in nums:
            new = max(prev1, prev2+num)
            prev2 = prev1
            prev1 = new
        return prev1
# @lc code=end
