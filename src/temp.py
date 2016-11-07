"""
70 Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Subscribe to see which companies asked this question

1 step -> 2 steps -> 1 step ... 
2 step -> 2 steps -> 2 step ...

f(5) -> 8

"""

class Solution(object):
    """
    Explanation:

    This problem is the Fibonacci sequence in disguise

    You have a recurrence relationship that is

    S_i = S_(i-1) + S_(i-2)

    and you have to solve it without blowing the stack,
    i.e. save the solution to previous sub problems

    O(n) Time
    O(n) Space

    """
    def climbStairs(self, n):

        """
        :type n: int
        :rtype: int
        """

        # Empty array to save solutions

        steps = [0 for _ in range(n+1)]

        # Set Base cases

        for num in (0,1,2):
            steps[num] = num

        # Solve sub problems

        for num in range(3,n+1):

            steps[num] = steps[num-1] + steps[num-2]

        # Return Solution

        return steps[n]


r = Solution()
res = r.climbStairs(5)
print (res)
