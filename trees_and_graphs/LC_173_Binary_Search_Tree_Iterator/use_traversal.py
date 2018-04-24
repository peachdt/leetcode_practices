# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root 
# node of a BST.

# Calling next() will return the next smallest number in the BST.

# Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height 
# of the tree.

"""
Run time: 123ms
This is my original answer. Since the output is essentially the inorder traversal of the tree, I'm doing a 
preorder traversal during initialization. And just pop the first item each time when calling for next().
The pro is that hasNext() and next() will be constant time, but the con is that memory is higher due to the 
storage of the whole tree in preorder.
"""
# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Code starts here: 
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.preorder = []
        self.getPreorder(root, self.preorder)
        self.inorder = sorted(self.preorder)
            
    def getPreorder(self, node, res):
        if node:
            res.append(node.val)
            if node.left:
                self.getPreorder(node.left, res)
            if node.right:
                self.getPreorder(node.right, res)
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if len(self.inorder) > 0 else False

    def next(self):
        """
        :rtype: int
        """
        return self.inorder.pop(0)
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())