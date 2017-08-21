class Solution(object):

    def lengthOfLastWord(self,s):

        stripped = s.strip().split()
        if len(stripped) == 0:
            return 0

        return len(stripped[-1])
