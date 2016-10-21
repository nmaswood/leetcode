from math import log,ceil

class Solution(object):
    def isPowerOfThree(self, n):
        
        
        if not n:
            return False
        n = abs(n)
        
        return (log(n) / log(3) + .001) % 1 <= 2 * .001
    


3  100

9  1001

27

81

243