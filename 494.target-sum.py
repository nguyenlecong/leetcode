#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
import functools


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @functools.cache
        def dfs(i=0, total=0):
            if i == len(nums):
                return total == target
            add = dfs(i+1, total+nums[i])
            sub = dfs(i+1, total-nums[i])
            return add + sub
        return dfs()
# @lc code=end
