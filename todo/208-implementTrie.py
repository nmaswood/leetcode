class TrieNode(object):
    def __init__(self, letter):
        self.root = letter
        self.end_of_a_word = False
        self.children = {}

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):

        def ins(tree, theWord):

            if not theWord:
                return TrieNode('')

            first, rest = theWord[0], theWord[1:]

            if first not in tree.children:
                tree.children[first] = TrieNode(first)

            return ins(rest, tree.children[first])

        return ins(self.root, word)

    def search(self, word):

        def s(tree, word):

            if not word:
                return True

            first, rest = word[0], word[1:]

            if first not in tree.children:
                return False

            return s(tree.children[first], rest)

        return s(self.root, word)

    def startsWith(self, word):

        return self.search(word)

