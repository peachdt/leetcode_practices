# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding 
# window.

# For example,
# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3

"""
Run time: 76ms
Pretty straightforward question.
When initializing, size will be the size of the moving window.
Create a queue to store number in the next() call. When a new number getting added, update self.sum
If length of the queue is larger than window size, pop the first element from queue and minus its value
from self.sum.
"""

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.q = []
        self.sum = 0
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.sum += val
        self.q.append(val)
        if len(self.q) > self.size:
            self.sum -= self.q.pop(0)
            return self.sum / float(self.size)
        else:
            return self.sum / float(len(self.q))
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)