# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted 
# order, not the kth distinct element.

# For example,
# Given [3,2,1,5,6,4] and k = 2, return 5.

# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.

"""
Run time: 157ms

Use merge sort. This solution can also be done using in-place sorting for better space complexity.
Idea is to use merge sort to sort the array, and access the kth element from the right side.
For very large array, use in-place sorting to have O(nlogn) time, and O(1) space.
"""

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        x = self.mergeSort(nums)
        index = len(x) - k
        
        return x[index]
    
    def mergeSort(self, nums):
        result = []
        n = len(nums)
        if n < 2:
            return nums
        mid = (n-1) // 2
       
        l = self.mergeSort(nums[0:mid+1])
        r = self.mergeSort(nums[mid+1:])
        return self.merge(l, r, result)
            

    def merge(self, l1, l2, result):
        l = len(l1)
        r = len(l2)
        i = j = 0
        while i < l and j < r:
            if l1[i] < l2[j]:
                result.append(l1[i])
                i += 1
            else:
                result.append(l2[j])
                j += 1
        while i < l:
            result.append(l1[i])
            i += 1
        while j < r:
            result.append(l2[j])
            j += 1
        return result
        
        