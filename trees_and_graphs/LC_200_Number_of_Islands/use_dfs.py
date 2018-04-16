# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

# Example 1:
# 11110
# 11010
# 11000
# 00000
# Answer: 1

# Example 2:
# 11000
# 11000
# 00100
# 00011
# Answer: 3

"""
Run time: 132ms

Loop through m, n with i, j, if grid[i][j] is "1", do DFS on this point. count += 1.
In dfs function, mark current position to "#". Do dfs on 4 directions: left, right, top, down. Break condition
is if i or j is out of bound, or neighbor is not "1".
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        m,n = len(grid), len(grid[0])
        count = 0
        
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == "1":
                    count += 1
                    self.dfs(i, j, grid)
        return count
        
    def dfs(self, i, j, grid):
        # break condition
        if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1 or grid[i][j] != "1":
            return
        
        grid[i][j] = "#"
        # left
        self.dfs(i, j-1, grid)
        # right
        self.dfs(i, j+1, grid)
        # up
        self.dfs(i-1, j, grid)
        # down
        self.dfs(i+1, j, grid)
        