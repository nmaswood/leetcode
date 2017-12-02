class Node():
    def __init__(self, value):
        self.value = value
        self.children = set()

    def __contains__(self, value):

        return val in self.children

    def get_from_children(self, key):

        for node in self.children:

            if node.value == key:
                return node

        raise Exception()

    def insert(self, value):

        def _insert(head, word):

            if not word:
                return

            letter, word_prime = letter[0], word_prime[1:]

            if letter not in head.children:
                new_node = Node(letter)
                head.children.add(new_node)
                _insert(new_node, word_prime)
            else:
                new_head = self.get_from_children(letter)
                _insert(new_head, letters)

        _insert(self, value)

class Solution(object):

    def __init__(self):

        self.root = Trie()

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: st
        """

        self._insert_words(strs)

        acc = ''

        def traverse(tree):


            if len(tree.children):

                acc += tree.children.keys()
                        pass

test = ['foo', 'foobar', 'foobaz']
