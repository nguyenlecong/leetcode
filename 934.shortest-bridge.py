#
# @lc app=leetcode id=934 lang=python3
#
# [934] Shortest Bridge
#

# @lc code=start
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        r, c = self.find_first_land(grid)
        self.mark_island_as_2(grid, r, c)

        N = len(grid)
        island_1_lands = set((r, c)
                             for r in range(N)
                             for c in range(N)
                             if grid[r][c] == 1)

        dist = 0
        while island_1_lands:
            new_island_1_lands = set()
            for r, c in island_1_lands:
                for x, y in (r-1, c), (r+1, c), (r, c-1), (r, c+1):
                    if not(0 <= x < N and 0 <= y < N):
                        continue

                    if grid[x][y] == 0:
                        grid[x][y] = -dist-1
                        new_island_1_lands.add((x, y))
                    elif grid[x][y] == 2:
                        return dist
            dist += 1
            island_1_lands = new_island_1_lands

    def find_first_land(self, grid):
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return (r, c)

    def mark_island_as_2(self, grid, r, c):
        grid[r][c] = 2
        for x, y in (r-1, c), (r+1, c), (r, c-1), (r, c+1):
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                self.mark_island_as_2(grid, x, y)

# @lc code=end
