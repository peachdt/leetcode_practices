# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
# Example:

# Given the sorted linked list: [-10,-3,0,5,9],

# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

#       0
#      / \
#    -3   9
#    /   /
#  -10  5

"""
Run time: 290ms
Use two pointers, slow and fast, to find the mid point of the linked list.
This mid point, slow.next, will be the root of the BST.
Cut the left half before mid point for root's left child, and the rest of the linked list will be 
root's right child.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Code starts here:
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return 
        if not head.next:
            return TreeNode(head.val)
        
        slow, fast = head, head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        temp = slow.next
        root = TreeNode(temp.val)
        slow.next = None
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(temp.next)
        return root