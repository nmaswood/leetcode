class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        no_spaces = ' '.join(s.split(" "))
        
        return ' '.join(no_spaces.split(" ")[::-1])
        
        