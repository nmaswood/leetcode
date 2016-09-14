class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        a = {}
        
        for index, num in enumerate(nums):
            
            if num in a:
                if index - a[num] <= k:
                    return True
            a[num] = index
            
        return False