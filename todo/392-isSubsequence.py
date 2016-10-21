class Solution(object):
    def isSubsequence(self, s, t):

        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        i, j = 0, 0

        while j < len(t) and i < len(s):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)
r = Solution()

res = r.isSubsequence('FUCK', 'FUCKYOU')

print (res)



