# There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. 
# You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. 
# Derive the order of letters in this language.

# Example 1:
# Given the following words in dictionary,

# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]
# The correct order is: "wertf".

# Example 2:
# Given the following words in dictionary,

# [
#   "z",
#   "x"
# ]
# The correct order is: "zx".

# Example 3:
# Given the following words in dictionary,

# [
#   "z",
#   "x",
#   "z"
# ]
# The order is invalid, so return "".

# Note:
# You may assume all letters are in lowercase.
# You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return any one of them is fine.


"""
Run time: 40ms

Use topological sorting. Create a graph with nodes as all letters in the dictionary. Each node has IN and OUT, suggesting its relative position with another letter.
Commented out code is the same as its above, just a smarter way of using Python's zip function to iterate through list of dictionary to find edges.
Instead of traditionally move through all connected nodes until the very last one and put into a stack, this method checks if a node has IN or not. If not, which means position should be in the front, got removed and attached to 
result right away. Then this node will be deleted from the whole graph, and keep iterating other nodes. If the size of the tree did not get shrinked after one iteration, means it has a cycle in it, and return ""
"""


class Node(object):
    def __init__(self):
        self.IN = set()
        self.OUT = set()

class Solution(object):
    def alienOrder(self, words):
       # find out nodes
        graph = {}
        for word in words:
            for letter in word:
                if letter not in graph:
                    graph[letter] = Node()

        # find out directed edges (from StefanPochmann)
        left = 0

        while left < len(words) - 1:
            index_max = min(len(words[left]), len(words[left + 1]))
            index = 0
            while index < index_max:
                if words[left][index] == words[left + 1][index]:
                    index += 1
                else: 
                    graph[words[left][index]].OUT.add(words[left + 1][index])
                    graph[words[left + 1][index]].IN.add(words[left][index])
                    break
            left += 1

        # # find out directed edges (from StefanPochmann)
        # for pair in zip(words, words[1:]):
        #     for a, b in zip(*pair):
        #         if a != b:
        #             graph[a].OUT.add(b)
        #             graph[b].IN.add(a)
        #             break

        # topo-sort
        res = ""
        while graph:
            oldlen = len(graph)

            for key in graph:
                if not graph[key].IN:   # to remove this
                    for key2 in graph[key].OUT:
                        graph[key2].IN.remove(key)
                    del graph[key]
                    res += key
                    break

            if oldlen == len(graph): # if shrinking stops, solution doesn't exist
                return ""
            oldlen = len(graph)
        return res