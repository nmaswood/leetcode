from itertools import permutations
class Solution():

	def __init__(self):
		pass

	def pluck(self, word, index):

		return [x for (idx,x) in enumerate(word) if idx != index]

	def permutations_size_k(self, word, k):

		l_word = len(word)

		if k > l_word:
			return []

		acc = set()

		def recurse(rest,seen, total):

			if total == k or not rest:
				acc.add(seen)
				return


			for (index, letter) in enumerate(rest):

				plucked = self.pluck(rest, index)

				letter = rest[index]

				seenPrime = seen + letter

				recurse(plucked, seenPrime, total + 1)

		recurse(word, '', 0)

		return acc

r = Solution()
res = r.permutations_size_k('abcd',3)
print (res)
res  = permutations('abcd', 3)
print ([''.join(x) for x in res])