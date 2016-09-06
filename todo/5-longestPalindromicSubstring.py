class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        l = len(s) + 1

        words = [(s[i:j], j - i) for i in range(l) for j in range(i,l) if not i == j and s[i:j] == s[i:j][::-1]]

        return max(words, key = lambda x: x[1])[0]



r = Solution()

r.longestPalindrome('ABCBD')
