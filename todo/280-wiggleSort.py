class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        l = len(nums)
        left, right = 0, l - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 2
            right -= 2

        return nums

r = Solution()
res = r.wiggleSort([3,5,2, 1,6,4])

print (res)

