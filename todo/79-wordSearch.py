class Solution(object):

    def children(self, board, index):

        NUM_ROWS = len(board)
        NUM_COLS = len(board[0])

        x, y = index

        children = [
            (x,y + 1),
            (x,y - 1),
            (x - 1, y),
            (x + 1, y)
        ]

        return [(i,j) for i, j in children if 0 <= i < NUM_ROWS and 0 <= j < NUM_COLS]

    def searchMatrix(self,string, index, board, visited):

        if not string:
            print (visited)
            return True

        head, tail = string[0], string[1:]

        left, right = index

        copy = set(visited)
        copy.add(index)

        if head != board[left][right]:
            return False

        children = self.children(board, index)

        for child in children:
            if child not in visited:

                if self.searchMatrix(tail, child, board, copy):
                    return True

        if not children and not tail:
            return True

        return False


    def exist(self, board, word):

        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            for j in range(cols):

                if self.searchMatrix(word, (i,j), board, set()):
                    return True

        return False


r = Solution()
array = ["aaa"]
s = "aaa"
res = r.exist(array, s)
print (res)
