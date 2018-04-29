# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. 
# The algorithm should run in linear time and in O(1) space.

"""
Run time: 68ms

Idea is to create a dictionary to store number and its count. O(n) time, but O(n) space.
"""

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        res = []
        for num, count in d.items():
            if count > n/3:
                res.append(num)
                
        return res
        
        
        