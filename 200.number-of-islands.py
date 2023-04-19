#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
from re import L


class Solution:
    # DFS
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     R, C = len(grid), len(grid[0])

    #     def sink_island(r, c):
    #         grid[r][c] = "0"
    #         for x, y in (r, c-1), (r, c+1), (r-1, c), (r+1, c):
    #             if 0 <= x < R and 0 <= y < C and grid[x][y] == "1":
    #                 sink_island(x, y)

    #     cnt = 0
    #     for r in range(R):
    #         for c in range(C):
    #             if grid[r][c] == "1":
    #                 sink_island(r, c)
    #                 cnt += 1
    #     return cnt

    # BFS
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])

        def sink_island(r, c):
            queue = [(r, c)]
            i = 0
            for x, y in queue:
                i += 1
                if 0 <= x < R and 0 <= y < C and grid[x][y] == "1":
                    grid[x][y] = "0"
                    queue.extend([(x, y-1), (x, y+1), (x-1, y), (x+1, y)])

        cnt = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1":
                    sink_island(r, c)
                    cnt += 1
        return cnt
        # @lc code=end


# grid = [
#     ["1", "1", "0", "0", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "1", "0", "0"],
#     ["0", "0", "0", "1", "1"]
# ]
# a = Solution()
# cnt = a.numIslands(grid)
# print(cnt)
