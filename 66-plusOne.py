class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        as_str = ''.join([str(x) for x in digits])

        print (as_str)

        as_int = int(as_str) + 1

        as_str_prime = str(as_int)


        return [int(x) for x in list(as_str_prime)]


#r = Solution()

#x = r.plusOne([1,1])

#print (x)
