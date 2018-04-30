# Given an array nums, there is a sliding window of size k which is moving from the very left of the array 
# to the very right. You can only see the k numbers in the window. Each time the sliding window moves right 
# by one position.

# For example,
# Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Therefore, return the max sliding window as [3,3,5,5,6,7].

# Note: 
# You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for non-empty array.

"""
Run time: 166 ms

Not really a well defined question. Intension of it is to use heap, but somehow when I use heapq it exceeds
time limit.

So for this solution, use max instead. Find max of initial window and add to res.
Then iterate from kth to n-1 th number. If new number nums[i] is larger than tempMax, set tempMax to it.
If nums[i] equals or is smaller than tempMax, do nothing.
One condition to think about is that since window is moving towards right, the left value will leave window.
If the number which just left the window is the largest, we need to find new tempMax for current window, which
is from index (i-k+1) to (i+1)
"""

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        res = []
        
        if n == 0:
            return res
        
        tempMax = max(nums[:k])
        res.append(tempMax)
        
        for i in range(k, n):
            if nums[i] > tempMax:
                tempMax = nums[i]
            elif tempMax == nums[i-k]:
                tempMax = max(nums[i-k+1:i+1])
            
            res.append(tempMax)
        return res
        