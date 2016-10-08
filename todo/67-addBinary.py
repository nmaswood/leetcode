from itertools import zip_longest

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        acc = []
        carry = 0

        for value1, value2 in zip_longest(a[::-1], b[::-1], fillvalue = None):

        	value1 =  0 if value1 is None else int(value1)
        	value2 =  0 if value2 is None else int(value2)

        	sum_val = value1 + value2 + carry

        	if sum_val == 0:
        		res = '0'
        		carry = 0
        	elif sum_val == 1:
        		res = '1'
        		carry = 0
        	elif sum_val == 2:
        		res = '0'
        		carry = 1
        	elif sum_val == 3:
        		res = '1'
        		carry = 1

        	acc.append(res)

        if carry:
        	acc.append('1')

        return ''.join(acc[::-1])