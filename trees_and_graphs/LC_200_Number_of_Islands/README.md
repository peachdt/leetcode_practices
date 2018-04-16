# LC 200 Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
Example 1:

> 1 1 1 1 0

> 1 1 0 1 0

> 1 1 0 0 0

> 0 0 0 0 0

Answer: 1

Example 2:

> 1 1 0 0 0

> 1 1 0 0 0

> 0 0 1 0 0

> 0 0 0 1 1

Answer: 3

---
This problem can be solved by using DFS and BFS.

Solutions included are both DFS, one use extra O(M*N) space for keeping visited map, and another one without extra space, but loop through grid approximately twice (once for loop m and n, once for dfs on whole grid).
