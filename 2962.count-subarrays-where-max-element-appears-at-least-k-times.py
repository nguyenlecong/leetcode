#
# @lc app=leetcode id=2962 lang=python3
#
# [2962] Count Subarrays Where Max Element Appears at Least K Times
#

# @lc code=start

import collections

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = left = 0
        mx = max(nums)
        counter = collections.Counter()
        for num in nums:
            counter[num] += 1
            while counter[mx] > k or nums[left] != mx:
                counter[nums[left]] -= 1
                left += 1
            if counter[mx] >= k:
                ans += left + 1
        return ans
# @lc code=end

