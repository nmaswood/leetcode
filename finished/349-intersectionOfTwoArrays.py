class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums = [x for x in nums1 if x in nums1 and x in nums2]
        
        
        
        return list(set(nums))