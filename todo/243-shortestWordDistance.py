class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i = -1
        j = -1
        MIN = float('inf')
        words = ['empty'] + words

        for idx, word in enumerate(words):
            if idx == 0:
                continue

            if i != -1 and j != -1:
                MIN = min(MIN, abs(i -j))

            if word == word1:

                print (idx,word)
                i = idx
            elif word == word2:

                j = idx

        if i != -1 and j != -1:
            MIN = min(MIN, abs(i -j))


        return MIN

r = Solution()

res = r.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], 'makes', 'coding')

print (res)




