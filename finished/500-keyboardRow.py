class Solution(object):

    def __init__(self):

        self.rows = [
                {'q', 'w', 'e', 'r', 't','y','u','i','o', 'p'},
                {'a','s','d','f', 'g', 'h', 'j', 'k', 'l'},
                {'z', 'x', 'c', 'v', 'b', 'n', 'm'}]

    def checkRowWord(self,row,word):

        return all(letter in row for letter in word)

    def checkRows(self, word):

        return any(self.checkRowWord(row, word.lower()) for row in self.rows)

    def findWords(self, words):

        """
        :type words: List[str]
        :rtype: List[str]
        """

        return [word for word in words if self.checkRows(word)]

x = Solution()
Input = ["Hello", "Alaska", "Dad", "Peace"]
#Output: ["Alaska", "Dad"]

res = x.findWords(Input)
print (res)

