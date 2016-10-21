from collections import defaultdict


class Solution(object):

    def possible_letters_at_index(self, words):

        d = defaultdict(set)

        for word in words:

            for (idx, letter) in enumerate(word):

                d[idx].add(letter)

        return dict(d)


    def ladderLength(self, beginWord, endWord, wordList):

        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int

        """
        acc = []

        index_to_letter_dict = self.possible_letters_at_index(wordList.union(set([beginWord,endWord])))

        total_len = len(wordList)

        len_word = len(beginWord)

        print (index_to_letter_dict)


        def solve(current, end, seen, path, l):

            seen.add(current)

            if l == total_len:
                return None

            if begin == end:
                print ("fuck")
                return path

            for index in range(len_word):


                for letter in index_to_letter_dict[index]:

                    newWord = list(current)
                    newWord[index] = letter

                    newWord = ''.join(newWord)
                    if newWord == end:
                        acc.append(path + [current])
                        return

                    if newWord in wordList and  newWord not in seen:

                        pathPrime = list(path)
                        pathPrime.append(current)

                        if (solve(newWord, end, set(seen), pathPrime, l + 1)):
                            return True


        solve(beginWord, endWord, set(), [], 0)

        print (acc)
        if len(acc) == 0:
            print ("fuck")
            return 0
        s = [x for x in s if x != []]
        s = sorted(acc, key = lambda x: len(x))


        return len(s[0]) + 1



begin = "a"
end = "c"

l = set(['a','b','c'])

r = Solution()



x = r.ladderLength(begin, end, l)
print (x)














        