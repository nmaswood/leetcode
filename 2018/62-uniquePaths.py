class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        DP = [
            [0 for _ in range(m)]
            for _ in range(n)
        ]

        for m_sub in range(m):
            DP[0][m_sub] = 1

        for n_sub in range(n):
            DP[n_sub][0] = 1

        for row_n in range(1, n):
            for col_m in range(1, m):
                DP[row_n][col_m] = (
                    DP[row_n - 1][col_m] + DP[row_n][col_m-1]
                )
        return DP[-1][-1]


def board(rows):
    for row in rows:
        print(row)


x = Solution()

x.uniquePaths(7, 3)
