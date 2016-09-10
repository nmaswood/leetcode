class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        init_dict = {
            2: 2,
            1:1,
            0:0
        }

        def populate_dict(d):
            for k in range(3,n + 1):
                d[k] = d[k -1] + d[k-2]

        populate_dict(init_dict)

        return init_dict[n]


#r = Solution()
#r.climbStairs(5)
