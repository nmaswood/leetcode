class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False



        prev1 = s[0]
        prev2 = t[0]

        for l1,l2 in zip(s[1:],t[1:]):

            if l1 == prev1 and l2 != prev2:
                return False
            elif l1 != prev1 and l2 == prev2:
                return False

            prev1 = l1
            prev2 = l2

        return True



#r = Solution()
#x = r.isIsomorphic('foo', 'egg')
#print (x)
