class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        words = s.split()

        return ' '.join([word[::-1] for word in words])


