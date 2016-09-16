class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        row = len(matrix)
        col = len(matrix[0])

        T = [[0 for _ in range(row + 1)] for _ in range(col + 1)]
        maxArea = 0
        for i in range(row):
            for j in range(col):

                val = matrix[i][j]
                if val in ['1', 1]:
                    print (i,j)
                    T[i][j] = 1 if i == 0 else T[i-1][j] +1
        print (T)


r = Solution()
r.maximalRectangle([
    [1,0,1,0,0],
    [1,0,1,1,1],
    [1,1,1,1,1],
    [1,0,0,1,0],
])
