class Date():

	def __init__(self, raw):

		d,m,y = raw.split('-', 2)

		self.d = d
		self.m = m
		self.y = y

	def meth(self):
		pass

	def meth(self):
		pass

	def meth(self):

		pass
	def meth(self):
		pass

	def __sub__(self,other):
		return self.abs_days() - other.abs_days()



class Solution():

	def __init__(self):
		self.foo = 'bar'

	def find(self, binary_tree, find_me):


		def _find(root, looking_for, value):

			if not root:
				return None

			val, left, right = root.val, root.left, root.right


			if val == looking_for:

				if right is None:
					return value

				return right.val


			traverse_me_next = left if val > looking_for else right

			return _find(traverse_me_next, looking_for, val)

		res  = _find(binary_tree, find_me, None)

		if res is None:
			raise ValueError("Value was not found in tree")
			
		return res

































