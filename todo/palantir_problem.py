class Crypto():

	def __init__(self, s1, s2, s3):
		self.s1 = s1
		self.s2 = s2
		self.s3 = s3

	def to_number(self, word, proposed_dictionary):


		return int([proposed_dictionary[letter] for letter in word])

	def verify(self, proposed_dictionary):


		s1,s2,s3 = [self.to_number(x) for x in (self.s1,self.s2, self.s3)]

		return  s1 + s2 == s3


class Permute():


	def __init__(self):
		pass

	def pluck(self, word, index):

		return [x for i,x in enumerate(word) if i != index]

	def permute_size_k(self,word,k ):

		acc = set()

		def recurse(rest, seen_so_far, l):

			print (see)

			if not rest or l == k:
				acc.add(seen_so_far)
				return

			l_rest = len(rest)

			for i in range(l_rest):

				plucked = self.pluck(rest, i)
				print (plucked)

				seen_so_far_prime = seen_so_far + rest[0]

				recurse(plucked, seen_so_far_prime, l + 1)

		recurse(word, '', 0)

		return acc
r = Permute()

res = r.permute_size_k('abc',2)

print (res)


























