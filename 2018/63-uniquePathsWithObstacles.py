from pdb import set_trace


def board(b):
    for x in b:
        print(x)


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        num_cols, num_rows = len(obstacleGrid[0]), len(obstacleGrid)

        DP = [
            [0 for _ in range(num_cols)]
            for _ in range(num_rows)
        ]

        for col_i in range(num_cols):
            if obstacleGrid[0][col_i] == 1:
                break
            DP[0][col_i] = 1

        for row_i in range(num_rows):
            if obstacleGrid[row_i][0] == 1:
                break
            DP[row_i][0] = 1

        for row_i in range(1, num_rows):
            dp_row = DP[row_i]
            for col_i in range(1, num_cols):

                is_obstacle = obstacleGrid[row_i][col_i] == 1
                left = obstacleGrid[row_i][col_i - 1] == 1
                above = obstacleGrid[row_i - 1][col_i] == 1

                if is_obstacle:
                    continue
                acc = 0

                if not left:
                    acc += DP[row_i][col_i - 1]

                if not above:

                    acc += DP[row_i-1][col_i]

                dp_row[col_i] = acc

        return DP[-1][-1]


obstacle_input = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]

sol = Solution()

res = sol.uniquePathsWithObstacles(obstacle_input)
print (res)
