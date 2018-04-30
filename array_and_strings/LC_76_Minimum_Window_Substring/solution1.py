# Given a string S and a string T, find the minimum window in S which will contain all the characters in 
# T in complexity O(n).

# Example:

# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"

"""
Run time: 246 ms

Use Counter to find how many words it needs, and missing is the length of t.

Iterate through all chars in s, starting with index 1. If char in need count is larger than 0, decrease missing
and decrease the count in need.
When missing == 0, which means longer missing any chars, loop through s again, from index i == 0 while i < j,
and char at i in need is negative (which means current string has duplicate of char). Inside this while loop,
increase i, and increase the count of this char in need.
When the while loop breaks, which means either i == j or char is no longer duplicate (has to be in the substring).
check j -1 with J-I, which is the placeholder for minimum length. Update this minimum length if necessary.
"""

import collections
def minWindow(self, s, t):
    need, missing = collections.Counter(t), len(t)
    i = I = J = 0
    for j, c in enumerate(s, 1):
        if need[c] > 0:
            missing -= 1
        need[c] -= 1
        if not missing:
            while i < j and need[s[i]] < 0:
                need[s[i]] += 1
                i += 1
            if not J or j - i <= J - I:
                I, J = i, j
    return s[I:J]