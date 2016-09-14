from collections import Counter

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        a = Counter(s)
        b = Counter(t)
        
        for letter in set(t):
            if letter not in a:
                return letter
            else:
                if a[letter] != b[letter]:
                    return letter