#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []

        def generate(sofar="", op=0, cl=0):
            if op > n:
                return
            if cl > op:
                return
            if op == cl == n:
                ans.append(sofar)
            generate(sofar+"(", op+1, cl)
            generate(sofar+")", op, cl+1)
        generate()
        return ans
# @lc code=end
