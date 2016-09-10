class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = max(nums)
        
        
        
        actual_sum = sum(nums)
        expected_sum = n * (n + 1 ) / 2
        
        x = expected_sum - actual_sum
        
        
        if len(nums) == 1:
            if nums[0] == 1:
                return 0
                
        if x == 0: 
            return n + 1
        if 1 in 
        
        return x