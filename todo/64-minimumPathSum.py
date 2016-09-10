class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid[0])
        m = len(grid)

        acc = [[float('inf')] * (n) for _ in range(m)]

        acc[0][0] = grid[0][0]

        for i in range(1,n):
            acc[0][i] = acc[0][i- 1]  + grid[0][i]

        for i in range(1,m):
            acc[i][0] = acc[i-1][0] + grid[i][0]

        for j in range(1,n):
            for i in range(m):

                cost = grid[i][j]
                up_one = acc[i][j - 1]
                left_one = acc[i- 1][j]

                acc[i][j] = cost + min(up_one, left_one)

        return acc[-1][-1]

r = Solution()
res = r.minPathSum([[1,2,3],[4,5,6],[7,8,9]])
print (res)
