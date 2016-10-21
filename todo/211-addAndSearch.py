class Trie():

    def __init__(self):

        self.children = {}
        self.isWord = False


class WordDictionary(object):
    def __init__(self):

        self.root = Trie()
        

    def addWord(self, word):


        def addLetter(letter, trie):

            if not letter:
                trie.isWord = True
                return

            first, rest = letter[0], letter[1:]

            if first not in trie.children:
                trie.children[first] = Trie()

            addLetter(rest, trie.children[first])

        addLetter(word, self.root)
     

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """

        def find(word, trie):

            if not word:
                return True

            first, rest = word[0], word[1:]

            if first == '.':


                for letter, child in trie.children.items():

                    if find(rest, child):
                        return True

            elif first not in trie.children:
                return False
            else:

                return find(rest, trie.children[first])

        return find(word, self.root) or False


# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("ab")
res = wordDictionary.search("a.")




