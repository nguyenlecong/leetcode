#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
from unittest import result


class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        left = 0
        right = len(height) - 1

        while left < right:
            result = max(result, min(height[left], height[right])*(right-left))

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return result

# @lc code=end
