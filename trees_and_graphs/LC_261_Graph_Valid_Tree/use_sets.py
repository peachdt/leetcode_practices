# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
# write a function to check whether these edges make up a valid tree.

# For example:
# Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.
# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

# Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, 
# [0, 1] is the same as [1, 0] and thus will not appear together in edges.

# 
"""
Run time: 266ms

Create a set of itself for all numbers in n. 
Loop through each pair of edges, find index of the set where each edge is in. If two index are different, 
union these two sets.
If two indexes are the same, means there's a cycle, tree is not valid.
If number of edges is not n-1, tree is not valid
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
        
        sets = []
        for i in range(n):
            s = set()
            s.add(i)
            sets.append(s)
        for pair in edges:
            i = self.find(pair[0], sets)
            j = self.find(pair[1], sets)
            if i != j:
                self.union(i, j, sets)
            else:
                return False
        return True
        
    
    def find(self, n, sets):
        for set in sets:
            if n in set:
                return sets.index(set)
        
    def union(self, i, j, sets):
        sets[i] = sets[i].union(sets[j])
        del sets[j]