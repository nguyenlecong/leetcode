#
# @lc app=leetcode id=540 lang=python3
#
# [540] Single Element in a Sorted Array
#

# @lc code=start
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)//2
        while lo < hi:
            mid = (lo+hi)//2
            if nums[2*mid] == nums[2*mid+1]:
                lo = mid+1
            else:
                hi = mid
        return nums[lo*2]
# @lc code=end
