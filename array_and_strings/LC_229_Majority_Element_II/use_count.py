# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. 
# The algorithm should run in linear time and in O(1) space.

"""
Run time: 44ms

Idea is to create a set of all distinct numbers, and iterate through them to find their count.
"""
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        temp = list(set(nums))
        for num in temp:
            if nums.count(num) > len(nums)/3:
                res.append(num)
                
        return res
        