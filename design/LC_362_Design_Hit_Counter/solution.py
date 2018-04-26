# Design a hit counter which counts the number of hits received in the past 5 minutes.

# Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are 
# being made to the system in chronological order (ie, the timestamp is monotonically increasing). 
# You may assume that the earliest timestamp starts at 1.

# It is possible that several hits arrive roughly at the same time.

# Example:
# HitCounter counter = new HitCounter();

# // hit at timestamp 1.
# counter.hit(1);

# // hit at timestamp 2.
# counter.hit(2);

# // hit at timestamp 3.
# counter.hit(3);

# // get hits at timestamp 4, should return 3.
# counter.getHits(4);

# // hit at timestamp 300.
# counter.hit(300);

# // get hits at timestamp 300, should return 4.
# counter.getHits(300);

# // get hits at timestamp 301, should return 3.
# counter.getHits(301); 
# Follow up:
# What if the number of hits per second could be very large? Does your design scale?

"""
Run time: 38ms
My solution is to keep a hashtable with timestamp as key, and counts for hit as value, and an array just to 
keep track of timestamps.
If the system didn't specify when the data should exipre, for example all data before 10 min will be removed, 
I need to keep all the hits.
Limitation would be memory needed would keep growing as more hits are added.

Whenever a hit comes in, add it to both the hashtable, as well as the array. If multiple hits with same 
timestamp comes in, only one timestamp gets added to array, and count in the hashtable for this timestamp 
increase by one.
To get hits, I used a helper function to do binary search. Since timestamp is increasing monotonically, array
would be sorted already. Find the next index of the range (timestamp - 300), and use array slice to access the
qualifying timestamps in the array, lookup value in the hashtable.
"""

class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = {}
        self.timestamp_arr = []
        

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        if timestamp not in self.timestamp_arr:
            self.timestamp_arr.append(timestamp)
        if timestamp not in self.hits:
            self.hits[timestamp] = 1
        else:
            self.hits[timestamp] += 1
        

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        difference = timestamp - 300
        r = self.getRange(difference)
        count = 0
        if r >= len(self.timestamp_arr):
            return 0
        else:
            for time in self.timestamp_arr[r:]:
                count += self.hits[time]
            return count
        
        
    def getRange(self, difference):
        if difference > 0:
            left, right = 0, len(self.timestamp_arr) - 1
            while left <= right:
                mid = (left + right) // 2
                
                if self.timestamp_arr[mid] > difference:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        return 0
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)