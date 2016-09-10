from sys import exit
class Solution(object):
    def minDistance(self, word1, word2):

        if len(word2) > len(word1):
            word1, word2 = word2, word1
        print (word1, word2)
        exit()


        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        l1 = len(word1)
        l2 = len(word2)

        b = [[0] * (l1 + 1)] * (l2 + 1)

        for i in range(l1 + 1):
            b[0][i] = i

        for j in range(l2 + 1):
            b[j][0] = j

        for i in range(1,l1):
            for j in range(1,l2):

                let_i = word1[i]
                let_j = word2[j]

                replace = int(let_i != let_j)

                print ('j',j)
                print ('i',i)
                b[i][j] = min(
                    replace + b[i-1][j-1],
                    1 + b[i][j-1],
                    1 + b[i-1][j],
                )
        print (b[-1][-1])

r = Solution()
res = r.minDistance('horse', 'ros')

