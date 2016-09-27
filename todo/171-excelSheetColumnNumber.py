class Solution(object):
    def titleToNumber(self, s):

        """
        :type s: str
        :rtype: int
        """

        values = {chr(i): i - 64 for i in range(ord('A'), ord('A') + 26)}

        acc = 0

        for idx, value in enumerate(s):

            x = values[value]
            extra = idx * 25
            acc += x + extra

        return acc

r = Solution()
res = r.titleToNumber('C')
print (res)
