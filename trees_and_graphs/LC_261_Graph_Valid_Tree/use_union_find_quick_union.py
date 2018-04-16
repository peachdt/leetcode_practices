# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
# write a function to check whether these edges make up a valid tree.

# For example:
# Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.
# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

# Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, 
# [0, 1] is the same as [1, 0] and thus will not appear together in edges.

# 
"""
Run time: 36-50ms
Create an array as roots. Each number at its index has root as itself.
Loop through all edges, if roots of two edge are different, set the root of left edge to root of the right edge.
Helper function findRoot is used to recursively find the root of one number.

EX: n = 5, edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
num_list = [0, 1, 2, 3, 4]
after [0, 1] => [1, 1, 2, 3, 4]
after [1, 2] => [1, 2, 2, 3, 4]
after [2, 3] => [1, 2, 3, 3, 4]
after [1, 3] => root of position 1 = 2, root of position 2 = 3, root of position 3 = 3, stop. on the right side
                root of position 3 = 3. Both root equals, cycle detected.
"""
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n-1:
            return False

        num_list = [i for i in range(n)]
        for edge in edges:
            n1, n2 = edge[0], edge[1]
            n1_root, n2_root = self.findRoot(n1, num_list), self.findRoot(n2, num_list)
            if n1_root == n2_root:
                return False
            else:
                num_list[n1_root] = n2_root
        return True
    

    def findRoot(self, index, num_list):
        while index != num_list[index]:
            index = num_list[index]
        return index