# Implement a trie with insert, search, and startsWith methods.

# Note:
# You may assume that all inputs are consist of lowercase letters a-z.

"""
Run time: 298ms
Standard way of creating a trie with insert, search and startsWith.
Will be good to add delete method as well!
"""
# Code starts here:
import collections

class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.endOfWord = False

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current = self.root
        for c in word:
            node = current.children[c]
            if not node:
                node = TrieNode()
                current.children[c] = node
            current = node
        current.endOfWord = True
        
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for c in word:
            node = current.children.get(c)
            if not node:
                return False
            current = node
        return current.endOfWord
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for c in prefix:
            node = current.children.get(c)
            if not node:
                return False
            current = node
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)