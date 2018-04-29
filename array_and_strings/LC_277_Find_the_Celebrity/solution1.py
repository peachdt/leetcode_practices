# Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one 
# celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does 
# not know any of them.

# Now you want to find out who the celebrity is or verify that there is not one. The only thing you are 
# allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. 
# You need to find out the celebrity (or verify there is not one) by asking as few questions as possible 
# (in the asymptotic sense).

# You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function 
# int findCelebrity(n), your function should minimize the number of calls to knows.

# Note: There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there 
# is a celebrity in the party. If there is no celebrity, return -1.

""" 
Run time: 1402 ms

First find the potential celebrity by iterating through n and check if x knows i, with x starting at 0.
What it does is that, if x knows i, x = i. if x does not know i, keep x. This is because celebrity should not 
know anyone.

After getting potential celebrity x, since the first round get rid of all other people after x, we only need
to check if x knows anyone from 0-x. If so, x is not celebrity and return -1.
Then check if from 0-n if everyone knows x, if not, return -1. Otherwise, x is celebrity
"""

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 0
        for i in xrange(n):
            if knows(x, i):
                x = i
        if any(knows(x, i) for i in xrange(x)):
            return -1
        if any(not knows(i, x) for i in xrange(n)):
            return -1
        return x
       