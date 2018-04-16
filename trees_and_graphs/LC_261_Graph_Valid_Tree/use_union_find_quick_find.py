# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
# write a function to check whether these edges make up a valid tree.

# For example:
# Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.
# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

# Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, 
# [0, 1] is the same as [1, 0] and thus will not appear together in edges.

# 
"""
Run time: 300ms
Idea is to use array to represent connection between edges.
Create an array from 0 to n-1.
For each pair of edges, node 1 is edge[0], node 2 is edge[1]
if node_1_value == node_2_value, return False since we encounter a cycle.
if node_1_value != node_2_value, we iterate through num_list array, and change all nodes that has node_1_value
    to node_2_value.
EX:
n = 5, edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
num_list = [0, 1, 2, 3, 4]
after edge [0, 1] => [1, 1, 2, 3, 4]
after edge [1, 2] => [2, 2, 2, 3, 4]
after edge [2, 3] => [3, 3, 3, 3, 4]
after edge [1, 3] => position 1 == 3, position 3 == 3, found cycle
"""
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n - 1:
            return False
        
        num_list = [i for i in range(n)]
        
        for edge in edges:
            n1, n2 = edge[0], edge[1]
            n1_value, n2_value = num_list[n1], num_list[n2]
            
            if n1_value == n2_value:
                return False
            else:
                for node, node_value in enumerate(num_list):
                    if node_value == n1_value:
                        num_list[node] = n2_value
        return True 