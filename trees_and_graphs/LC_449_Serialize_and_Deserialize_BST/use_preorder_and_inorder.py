# Serialization is the process of converting a data structure or object into a sequence of bits so that it 
# can be stored in a file or memory buffer, or transmitted across a network connection link to be 
# reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how 
# your serialization/deserialization algorithm should work. You just need to ensure that a binary search 
# tree can be serialized to a string and this string can be deserialized to the original tree structure.

# The encoded string should be as compact as possible.

# Note: Do not use class member/global/static variables to store states. Your serialize and deserialize 
# algorithms should be stateless.


"""
Run time: 178ms
The basic idea is to rebuild the tree from deserialization. From LC 105 we can build a tree by having
its preorder and inorder values. 
Start by doing a preorder traversal on the tree, and since it's a BST, simply sort the result will give
me the inorder values.
Then just have a helper function to build the tree with preorder and inorder values.
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Code starts here:
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preorder(node):
            if node:
                result.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
                
        result = []
        preorder(root)
        return ' '.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        preorder = map(int, data.split())
        inorder = sorted(preorder)
        return self.buildTree(preorder, inorder)
    
    def buildTree(self, preorder, inorder):
        if inorder:
            index = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[index])
            root.left = self.buildTree(preorder, inorder[0:index])
            root.right = self.buildTree(preorder, inorder[index+1:])
            return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))