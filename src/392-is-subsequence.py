class Solution(object):
    def isSubsequence(self, s, t):

        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        len_s = len(s)
        len_t = len(t)

        if len_s == 0:
            return True
        elif len_s > len_t:
            return False

        i = 0

        for index, char in enumerate(t):

            if i == len_s:
                return True
            elif char == s[i]:
                i += 1

        return i == len_s

r = Solution()
# s, t = "abc", "ahbgdc"
s, t = "axc", "ahbgdc"
res = r.isSubsequence(s,t)
print (res)
