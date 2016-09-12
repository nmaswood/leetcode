from collections import Counter

class Solution(object):
    def canPermutePalindrome(self, s):
        
        if len(s) == 1:
            return True
        c = Counter(s)
        """
        :type s: str
        :rtype: bool
        """
        return any([v >= 2 for k,v in c.items()])
        