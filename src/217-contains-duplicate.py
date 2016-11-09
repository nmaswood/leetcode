"""
217. Contains Duplicate


[1,2,3,1] -> True

[1,2,3] ->  False
"""

class Solution(object):
    def containsDuplicate(self, nums):

        """
        Expalanation
        O(n) Time
        O(n) Space

        Walk through the list keeping track of elements seen
        If you ever see the same element twice return True

        :type nums: List[int]
        :rtype: bool
        """

        seen = set()

        for num in nums:

        	if num in seen:
        		return True

        	seen.add(num)

        return False