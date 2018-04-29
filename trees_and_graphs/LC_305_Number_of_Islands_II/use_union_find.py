# A 2d grid map of m rows and n columns is initially filled with water. 
# We may perform an addLand operation which turns the water at position (row, col) into a land. 
# Given a list of positions to operate, count the number of islands after each addLand operation. 
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

# Example:

# Given m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]].
# Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

# 0 0 0
# 0 0 0
# 0 0 0
# Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

# 1 0 0
# 0 0 0   Number of islands = 1
# 0 0 0
# Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

# 1 1 0
# 0 0 0   Number of islands = 1
# 0 0 0
# Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

# 1 1 0
# 0 0 1   Number of islands = 2
# 0 0 0
# Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

# 1 1 0
# 0 0 1   Number of islands = 3
# 0 1 0
# We return the result as an array: [1, 1, 2, 3]

"""
Run time: 500 ms

First create a Union class, initialize it's id dict, size dict, and count.
Change each position in positions to tuple as one object, for better manipulation.
For each position, add it to the Union class, islands.

In Union.add() function, it simply add the p to self.id[p], set size of this p, self.size[p] to 1, and 
increase overall land count.

Use a clever way to find all position's four neightbors, by using dp in (0,1), (0, -1), (1,0) nd (-1,0), and
add p[0] with dp[0] and p[1] with dp[1] as tuple. Since we treat position as one tuple, we don't need to think
about conditions for position to have over boundary indexes.
If any neighbor of this position already in islands.id dict, which means position connects with existing
land, do a union with this position and its neighbor (the existing land).

In the Union.union() function, first we use find() to find the root of both positions, i and j.
If i == j, which means they are already connected, simply return and exit.
If i != j, we need to connect these two lands and decrease island total count by 1.
    To connect i and j, we do an optimization which if size[i] > size[j] we merge j into i, 
    or if size[i] < size[j] we merge i into j. This is just an optimization.
Connecting two lands is basically set id[i] = j, since both i and j are the root of both lands. Then propagate
the size of one island to another.

In the Union.find() function, we find i's root by checking if id[i] equals to i itself. It is true if this island
is isolated, without connecting to other islands. But if not, use a while loop to find its root.
    Another optimization here is to use path compression. Instead of just doing i = self.id[i] in the while loop,
    we set self.id[i] = self.id[self.id[i]] first so that if we have a->b->c, it becomes a->c afterwards.
"""
class Union(object):
    def __init__(self):
        self.id = {}
        self.size = {}
        self.count = 0
        
    def add(self, position):
        # position in tuple, as (0,0)
        self.id[position] = position
        self.size[position] = 1
        self.count += 1
        
    def find(self, i, j,):
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]

        while j != self.id[j]:
            self.id[j] = self.id[self.id[j]]
            j = self.id[j]
        return i, j
            
    
    def union(self, position, neighbor):
        parent_of_position, parent_of_neighbor = self.find(position, neighbor)
        if parent_of_position == parent_of_neighbor:
            return
        if self.size[parent_of_position] > self.size[parent_of_neighbor]:
            parent_of_position, parent_of_neighbor = parent_of_neighbor, parent_of_position
        self.id[parent_of_position] = parent_of_neighbor
        self.size[parent_of_neighbor] += self.size[parent_of_position]
        self.count -= 1
        
class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        res = []
        islands = Union()
        for position in map(tuple, positions):
            # each position is in tuple, for example (0,0)
            islands.add(position)
            for dp in (0, 1), (0, -1), (1, 0), (-1, 0):
                neighbor = (position[0] + dp[0], position[1] + dp[1])
                if neighbor in islands.id:
                    islands.union(position, neighbor)
            res += [islands.count]
        return res
