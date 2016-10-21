class Solution(object):


    def toDict(self, pattern):

        letters = {}; numbers = {};

        numbers = [None for _ in range(len(pattern))]
        counter = 0


        for (index, letter) in enumerate(pattern):

            if letter not in letters:
                letters[letter] = counter
                counter += 1

            numbers[index] = letters[letter]

        return numbers


    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        list1 = self.toDict(pattern)
        list2 = self.toDict(str.split(" "))

        return list1 == list2



"abba"
"dog cat cat fish"
r = Solution()
res = r.wordPattern("abba", "dog cat cat fish")


print (res)
