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
Run time: 138ms

Same idea as use_dfs, but instead of marking current point as "#", create a visited map of same size as grid,
and set to all False.
While doing DFS, set point in visited map to True, and break condition includes if neighbor is already visited.
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        count = 0
        m,n = len(grid), len(grid[0])
        visited = [[False] * n for i in range(m)]
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    self.dfs(i, j, grid, visited)
                    count += 1
                    
        return count
    
    def dfs(self, i, j, grid, visited):
        if i < 0 or j < 0 or i > len(grid) -1 or j > len(grid[0]) - 1 or grid[i][j] != '1' or visited[i][j]:
            return
        visited[i][j] = True
        self.dfs(i, j-1, grid, visited)
        self.dfs(i, j+1, grid, visited)
        self.dfs(i-1, j, grid, visited)
        self.dfs(i+1, j, grid, visited)