# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root 
# node of a BST.

# Calling next() will return the next smallest number in the BST.

# Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height 
# of the tree.

"""
Run time: 90ms
Use stack to keep track of all the left child of the root and its children since they are the smallest
in a BST.
When calling next(), pop the stack, and check if this node has right child. For example, if root has no
left child and only one right child, then when root gets popped from stack, the next smallest node will be 
root's right child. Append this right child and move to this right child's left child. This is because in
BST left is always smaller than parent, and right. By doing so will make sure the right side of root gets 
checked properly.
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
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.stack) > 0

    # @return an integer, the next smallest number
    def next(self):
        node = self.stack.pop()
        x = node.right
        while x:
            self.stack.append(x)
            x = x.left
        return node.val
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())