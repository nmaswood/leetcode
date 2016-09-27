from math import floor

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        l_row = len(matrix[0])

        row_middle = floor(l_row - 1 / 2)

        def f(rest):

            len_rest = len(rest)

            if not rest or not len_rest:
                return False

            if len(rest) == 1:
                return target in rest[0]

            mid = floor(len_rest - 1 / 2)

            left, row, right=  rest[:mid], rest[mid], rest[mid:]

            first, mid, last = row[0], row[row_middle], row[-1]

            if target < first:
                return f(left)
            elif target > last:
                return f(right)
            else:
                return target in row

        return f(matrix)
r = Solution()
res = r.searchMatrix([[1,2],[3,4],[5,6]], 5)
print (res)




