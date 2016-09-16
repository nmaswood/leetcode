class WordDistance(object):
    def __init__(self, words):

        d = {word:[] for word in set(words)}

        for i, word in enumerate(words):
            d[word].append(i)

        self.d = d

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """

        x = self.d[word1]
        y = self.d[word2]

        diff1 = abs(max(x) - max(y))
        diff2 = abs(min(x) - min(y))

        return diff1 if diff1 < diff2 else diff2

Your WordDistance object will be instantiated and called as such:
wordDistance = WordDistance(words)
wordDistance.shortest("word1", "word2")
wordDistance.shortest("anotherWord1", "anotherWord2")
