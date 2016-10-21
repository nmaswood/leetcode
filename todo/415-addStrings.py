from itertools import zip_longest

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        carry = 0
        res  = ''

        for a,b in zip_longest(num1[::-1], num2[::-1]):

        	a = a or 0
        	b = b or 0

        	s = int(a) + int(b) + carry

        	carry = s // 10

        	a = s % 10

        	res +=  str(s % 10)

        return res[::-1]

r = Solution()
res = r.addStrings('111','1000')
print (res)