class Trie():

	def __init__(self):
		self.children = {}


class Solution(object):

	def __init__(self):

		self.root = Trie()

	def _insert_word(self, word):

		def _insert_letter(dictionary, letters):

			if not dictionary:
				return 

			first, rest = dictionary[0] ,dictionary[1:]


			if first not in dictionary.children:

				dictionary[first] = Trie()

			_insert_letter(d[first], rest)

		_insert_letter(self.root, word)

	def _insert_words(self, words):

		for word in words:

			self._insert_word(self.root, word)



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



















