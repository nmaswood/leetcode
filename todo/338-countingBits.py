from math import log

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        counter = 0
        acc = {0:0, 1:1}

        for n in range(1,num + 2):

            prev = acc[n-1]

            b = log(n,2) % 2
            print(n, b)

            new = prev + 1 if b else 1

            acc[n] = new

        return [acc[i] for i in range(n)]


r = Solution()
x = r.countBits(16)

print (x)
