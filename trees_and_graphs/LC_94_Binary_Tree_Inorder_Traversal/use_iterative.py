# Given a binary tree, return the inorder traversal of its nodes' values.

# For example:
# Given binary tree [1,null,2,3],
#    1
#     \
#      2
#     /
#    3
# return [1,3,2].

# Note: Recursive solution is trivial, could you do it iteratively?

"""
Run time: 30ms
Use stack to loop inorder iteratively. Put each node ins stack. If node has left child, move node to node.left. Otherwise, pop stack, and move to node.right.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        s = []

        while s or root:
            if root:
                s.append(root)
                root = root.left
            else:
                tmpNode = s.pop()
                result.append(tmpNode.val)
                root = tmpNode.right

        return result