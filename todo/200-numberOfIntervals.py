class Solution(object):

    def getNeighbors(self, point, xLim, yLim):

        i,j = point

        points = (

            (i + 1, j),
            (i - 1, j),
            (i, j - 1),
            (i, j + 1)
        )

        return ((x,y) for x,y in points if 0 <= x < xLim and 0 <= y <= yLim)

    def equalToZero(self, points):

        return all ([x == '0' for x in points])

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        cols = len(grid)
        rows = len(grid[0])

        curried = lambda x: self.getNeighbors(x, cols, rows)

        sols = set()

        for i in range(cols):

            for j in range(rows):
                print (curried(i,j))

                nearby = [grid[x][y] for x,y in curried((i,j))]

                if grid[x][y] == '1' and self.equalToZero(nearby):

                    sols.add((i,j))

        return list(sols)





