#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        tmp = x
        new_x = 0
        while tmp:
            new_x = new_x * 10 + tmp % 10
            tmp //= 10
        
        return new_x == x
# @lc code=end

