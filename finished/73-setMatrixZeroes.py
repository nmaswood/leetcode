class Solution(object):
    def setZeroes(self, matrix):

        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        len_rows = len(matrix)
        len_cols = len(matrix[0])

        rows = [False for _ in range(len_rows)]
        cols = [False for _ in range(len_cols)]

        for i in range(len_rows):
            for j in range(len_cols):

                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True

        for row_index, row in enumerate(rows):

            if row:

                for index in range(len_cols):
                    matrix[row_index][index] = 0

        for col_index, col in enumerate(cols):

            if col:

                for index in range(len_rows):
                    matrix[index][col_index] = 0

r = Solution()
A = [[1,2,0],[2,3,4],[5,6,7]]
r.setZeroes(A)
