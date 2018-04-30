# Given a string S and a string T, find the minimum window in S which will contain all the characters in 
# T in complexity O(n).

# Example:

# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"

"""
Run time: 160 ms

This solution replace the use of collections.Counter(), which made runtime faster.
Use simple iterative function to find all chars neede, and missing count.

First set minimum length to be len(s) + 1, which is the largest length needed.
While right index is less than length of s, or nothing is missing, check:
    1. if missing > 0, which means right need to keep moving right, check if word in t and the need of this 
    word is greater than 0. If so, update need word count, and missing count -= 1.
    2. if not missing anything and left < right, start moving left index. If word at left index in t, and if
    need of this word is greater or equal to 0, then we add 1 to missing, since the left index dropped one of
    the needed word, and update count in need for this word as well.
    3. final check the length between left and right. If right - left is smaller than preset minLength, then
    update start, end accordingly from left and right.
Return the array slice [start:end] if shorter substring was found, and "" if not.
"""

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = {}
        missing = 0
        
        for c in t:
            if c not in need:
                need[c] = 1
            else:
                need[c] += 1
            missing += 1
        
        left, right, start, end = 0, 0, 0, 0
        minLength = len(s) + 1
        while right < len(s) or missing == 0:
            if missing > 0:
                word = s[right]
                right += 1
                if word in t:
                    if need[word] > 0:
                        missing -= 1
                    need[word] -= 1
            elif missing == 0 and left < right:
                word = s[left]
                if word in t:
                    if need[word] >= 0:
                        missing += 1
                    need[word] += 1
                left += 1
            
            if missing == 0:
                if right-left < minLength:
                    minLength = right-left
                    start, end = left, right
                    
        return s[start:end] if minLength < len(s) + 1 else ""
        
        