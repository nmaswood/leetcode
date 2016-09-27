from sys import exit
class Solution(object):
    def correctOrder(self,word1,word2):
        if len(word1) > len(word2):
            return word1, word2
        return word2, word1
    def minDistance(self, word1, word2):

        # make sure words are in correct order by len
        word1, word2 = self.correctOrder(word1,word2)
        if len(word2) > len(word1):
            word1, word2 = word2, word1

        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        l1 = len(word1)
        l2 = len(word2)

        # Intialize matrix to save values

        T = [[0 for _ in range(l1 + 1)] for _ in range(l2 + 1)]


        # Initialize Base Steps
        for i in range(l1 + 1):
            T[0][i] = i

        for j in range(l2 + 1):
            T[j][0] = j

        print (T)
        # Choose the minimum of insert replaceing and deleting
        for i in range(1,l1 + 1):
            for j in range(1,l2):

                let_i = word1[i]
                let_j = word2[j]

                replace = int(let_i != let_j)

                T[i][j] = min(
                    replace + T[i-1][j-1],
                    1 + T[i][j-1],
                    1 + T[i-1][j],
                )
        print (T)
        return T[-1][-1]

r = Solution()
res = r.minDistance('horse', 'horses')
print (res)
