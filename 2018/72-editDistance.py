class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        if len(word1) < len(word2):
            word1, word2 = word2, word1

        DP = [
            [float('inf') for _ in range(len(word1) + 1)] for
            _ in range(len(word2) + 1)
        ]

        for j in range(len(word1) + 1):
            DP[0][j] = j

        for i in range(len(word2) + 1):
            DP[i][0] = i

        for j, l_j in enumerate(word1, 1):
            for i, l_i in enumerate(word2, 1):
                factor = 0 if l_i == l_j else 1
                DP[i][j] = min(DP[i-1][j] + 1,
                               DP[i][j-1] + 1,
                               DP[i-1][j-1] + factor)

        return DP[-1][-1]


def board(rows):
    for row in rows:
        print(row)

sol = Solution()
word1 = ""
word2 = "a"
res = 3

res_prime = sol.minDistance(word1, word2)
print (res_prime)
