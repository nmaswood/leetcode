from itertools import combinations

def generate_subsequences(iterable):

	l = len(iterable)

	solutions = set()

	for i in range(l + 1):

		solutions |= set(combinations(iterable, i))

	return solutions


def pluck(word, index):

	return [x for i,x in enumerate(word) if i != index]
	
def recursive_generation(iterable):

	solutions = set()

	def sub(curr):

		if not curr:

			return

	sub(iterable)

	return solutions


res = generate_subsequences('1234')

print (res)