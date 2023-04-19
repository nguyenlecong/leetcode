#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        D = {}
        for i, num in enumerate(nums):
            if (target - num) in D:
                return (D[target - num], i)
            D[num] = i
# @lc code=end

