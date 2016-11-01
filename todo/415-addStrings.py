from itertools import zip_longest

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        reversed_num_a = num1[::-1]
        reversed_num_b = num2[::-1]

        acc = ''

        carry = 0

        print (reversed_num_a, reversed_num_b)

        for (num_a, num_b) in zip_longest(reversed_num_a,reversed_num_b, fillvalue = '0'):


        	print (num_a, num_b)


        	num_a_int, num_b_int = int(num_a), int(num_b)

        	num_sum = num_a_int + num_b_int + carry


        	acc += str(num_sum % 10)
        	carry = int(num_sum / 10)


        acc  += '1' if carry else ''

        return acc[::-1]

r = Solution()
res = r.addStrings('19300', '90999930')

print (res)


#321
#0321













