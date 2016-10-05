class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """

        l = len(s)

        return [s[i:j] for i in range(l) for j in range(l) if s[i:j] in wordDict]
