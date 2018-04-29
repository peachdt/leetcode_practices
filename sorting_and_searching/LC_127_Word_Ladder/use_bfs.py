# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest 
# transformation sequence from beginWord to endWord, such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# Note:

# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# Example 1:

# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]

# Output: 5

# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
# Example 2:

# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]

# Output: 0

# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""
Run time: 116 ms

Idea is to use BFS. Starting off by iterating through all words in wordList, find all the words in each
segments and add to dictionary. 
By segments, it means for example, wordList ["hot","dot","dog","lot","log"], first check for segments
from index 1 to end of the word, which have words consisted with _ot, _og.
Then do it for segments from index 0-1, and 2-end, such as h_t, d_t, d_g, l_t, l_g
Then do it the last time from index 0-2, such as ho_, do_, lo_.
Append all three of those dictionaries to array.

In the BFS part, create a new deque object(double-side queue), and 
add (word, distance) to the deque and iterate through the range of beginWord.
For each iteration, i, check the same index of the dictionary to get the correct corresponding words. If word
does not match endWord, and if word is not visited, add this word and d+1 in deque for BFS. 
"""

import collections
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # initial check
        if endWord not in wordList:
            return 0
        
        # add each partial word in dictionary and append to adj
        n = len(beginWord)
        adj = []
        for i in range(n):
            d = collections.defaultdict(list)
            for word in wordList:
                d[word[:i] + word[i+1:]].append(word)
            adj.append(d)
            
        # BFS
        q = collections.deque()
        q.append((beginWord, 2))
        visited = set([beginWord])
        while len(q) > 0:
            cur, d = q.popleft()
            for i in range(n):
                partialWord = cur[:i] + cur[i+1:]
                for word in adj[i][partialWord]:
                    if word == endWord:
                        return d
                    if word not in visited:
                        visited.add(word)
                        q.append((word, d+1))
        return 0
