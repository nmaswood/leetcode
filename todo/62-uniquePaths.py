class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        rows = m
        cols = n


        DP = [[0 for _ in range(rows)] for _ in range(cols)]

        for i in range(rows):
            DP[0][i] = 1

        for j in range(cols):
            DP[j][0] = 1

        for i in range(1, rows):
            for j in range(1, cols):
                DP[i][j] = DP[i-1][j] + DP[i][j-1]

        return DP[-1][-1]




