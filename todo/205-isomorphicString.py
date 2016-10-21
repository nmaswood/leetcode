class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False


        d = {}

        for a,b in zip(s,t):

            if a in d:

                if d[a] != b:
                    return False
            else:

                d[a] = b
        
        return True



r = Solution()
x = r.isIsomorphic('paper', 'title')
print (x)
