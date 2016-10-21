class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]

        """
        acc = [[1]]

        for i in range(numRows):
        	new_list = []

        	if i + 1 <= len(acc[-1]):

        		val = acc[-1][i + 1]

        		new_list.append(acc[-1][i] + acc[-1][i+1])

        	new_list

        return acc
r = Solution()
res = r.generate(4)

print (res)
