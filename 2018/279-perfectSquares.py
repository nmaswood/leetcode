class Solution(object):
    @staticmethod
    def perfectSquares(n):
        if n == 0:
            return [0]
        nums = []

        i = 1
        while True:
            squared = i ** 2
            if squared > n:
                return nums
            nums.append(squared)
            i += 1

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        perfectSquares = Solution.perfectSquares(n)

        len_squares = len(perfectSquares)

        DP = [
            [float('inf') for _ in range(n + 1)]
            for _ in range(len_squares + 1)
        ]

        for row_i in range(len_squares + 1):
            DP[row_i][0] = 0

        for row_i in range(1, len_squares + 1):

            value_i = perfectSquares[row_i - 1]

            for col_i in range(1, n + 1):

                value_new = float('inf')

                if value_i <= col_i:
                    value_new = 1 + DP[row_i][col_i - value_i]

                DP[row_i][col_i] = min(DP[row_i - 1][col_i], value_new)

        return DP[-1][-1]


input_val = 6665
sol = Solution()
res = sol.numSquares(input_val)
print (res)
