#
# @lc app=leetcode id=1022 lang=python3
#
# [1022] Sum of Root To Leaf Binary Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = 0
        stack = [(root, 0)]
        while stack:
            node, total = stack.pop()

            if not node:
                continue

            total = total*2 + node.val

            if node.left is node.right is None:
                ans += total
                continue

            stack.append((node.right, total))
            stack.append((node.left, total))

        return ans

# @lc code=end
