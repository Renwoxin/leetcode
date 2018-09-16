"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water,
and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes"
(water inside that isn't connected to the water around the island). One cell is a square with side length 1.
The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
"""

# 整体思路
# 根据1个点周围有四条，2个点连接在一起则减少2条边的思路
class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r = len(grid)
        w = len(grid[0])
        out = 0
        for i in range(r):
            for j in range(w):
                if grid[i][j] == 1:
                    out += 4
                    if i > 0 and grid[i - 1][j] == 1:
                        out -= 2
                    if j > 0 and grid[i][j - 1] == 1:
                        out -= 2
        return out


A = Solution()
B = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
C = A.islandPerimeter(B)
print(C)