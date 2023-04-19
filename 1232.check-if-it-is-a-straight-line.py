#
# @lc app=leetcode id=1232 lang=python3
#
# [1232] Check If It Is a Straight Line
#

# @lc code=start
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x0, y0), (x1, y1) = coordinates[:2]
        return all((x1 - x0)*(y - y1) == (x - x1)*(y1 - y0) for x, y in coordinates)
# @lc code=end
