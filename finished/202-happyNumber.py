class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def split_sum(n):

            return sum([int(x) ** 2 for x in list(str(n))])
        i = 0

        new_sum = split_sum(n)

        while i < 10:
            new_sum = split_sum(new_sum)
            i += 1

        print(new_sum)
        return i == 1

r = Solution()

r.isHappy(1)
