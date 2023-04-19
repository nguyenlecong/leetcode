#
# @lc app=leetcode id=697 lang=python3
#
# [697] Degree of an Array
#

# @lc code=start
import collections


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        counters = collections.Counter(nums)

        degree = max(counters.values())
        elements = [num for num, freq in counters.items() if freq == degree]

        first_i = {}
        last_i = {}
        for i, num in enumerate(nums):
            if num not in first_i:
                first_i[num] = i
            last_i[num] = i
        return min(last_i[num] - first_i[num] + 1 for num in elements)


# @lc code=end
