class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        def swap(i,j):

        	nums[i], nums[j] = nums[j], nums[i]


        l = len(nums)

        left, right = 0, len(nums) - 1 

        for i in range(l):

        	while nums[i] == 2 and i < right:
        		swap(i,right)
        		right -= 1

        	while nums[i] == 0 and i > left:
        		swap(i,left)
        		left += 1 

r = Solution()

a = [2,0,0,0,1,1,1,0,0,0,2,1,0,0]
res = r.sortColors(a)
print (a)