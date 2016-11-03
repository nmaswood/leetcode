"""
1.Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution.

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

class Solution():

    """
    Space: O(n)
    Time: O(n)

    Explanation:

    Iterate through every number in the list, while you are doing that
    initialize a dictionary that keeps track of every number you've seen
    and the index you've seen it at.

    Before you add a number to this dictionary first ask if you have seen
    the difference  between the number you are currently looking at the and the
    target number in your dictionary. If you have return the index of both numbers.

    """

    def twoSum(self, nums, target):

        numbersSeen = {}

        for (index, number) in enumerate(nums):

            difference = target-number

            if difference in numbersSeen:
                return (index, numbersSeen[difference])

            numbersSeen[number] = index

        return ()









