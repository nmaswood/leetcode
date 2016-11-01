class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1:
        	return 1

        left = 0 
        right = x

        iterations = 0


        while left < right and iterations < 1000:

        	mid = (left + right) / 2

        	value = mid ** 2 

        	if value  == x:
        		return int(mid)
        	elif value < x:
        		left = mid

        	else:
        		right = mid

        	iterations += 1

        return int(round(left))

r = Solution()
res = r.mySqrt(4)
print (res)














        
