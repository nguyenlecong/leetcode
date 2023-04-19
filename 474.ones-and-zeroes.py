#
# @lc app=leetcode id=474 lang=python3
#
# [474] Ones and Zeroes
#

# @lc code=start
import collections
from functools import cache
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        @cache
        def dp(i, ones, zeroes):
            if ones < 0 or zeroes < 0:
                return float("-inf")
            if i == len(strs):
                return 0

            skip = dp(i+1, ones, zeroes)

            one, zero = counters[i]["1"], counters[i]["0"]

            take = dp(i+1, ones-one, zeroes-zero)+1
            return max(take, skip)

        counters = [collections.Counter(s) for s in strs]
        return dp(0, n, m)
        # @lc code=end
