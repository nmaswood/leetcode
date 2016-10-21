from collections import Counter

class Solution(object):

    def longestPalindrome(self, s):


        """
        :type s: str
        :rtype: int
        """

        counts = Counter(s)

        evens = [(k,v) for k, v in counts if v % 2 == 0]
        odds = [(k,v) for k, v in counts if v % 2 != 0]





