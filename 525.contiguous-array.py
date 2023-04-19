#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#

# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        height = max_len = 0
        D = {0: 0}
        for i, num in enumerate(nums, 1):
            height += 1 if num else -1
            max_len = max(max_len, i - D.setdefault(height, i))
        return max_len
# @lc code=end
