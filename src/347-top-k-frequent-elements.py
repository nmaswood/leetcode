"""

347. Top K Frequent Elements

Given a non-empty array of integers, return the k most frequent elements.

For example,

Given [1,1,1,2,2,3] and k = 2, return [1,2].

"""

from collections import Counter

class Solution(object):

    """
    
    Explanation:

    Use the counter method to count the occurences of each value in 
    in the list nums. Then use the method most_common to get the top
    k most frequently appearing elements

    """

    def topKFrequent(self, nums, k):

        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]

        """

        counted = Counter(x)

        most_common_elements = counted.most_common(k)

        # [(1,3), (2,2)] for k = 2

        return [pair[0] for pair in most_common_elements]



