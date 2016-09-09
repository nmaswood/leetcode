class Solution(object):

    def mark(self, nums):

        prev = None

        t = 0

        for index, num in enumerate(nums):

            if num == prev:
                nums[index] = None
                t+=1

            prev = num

        return nums


    def next_dup(self, nums, i):

        for idx in range(i, len(nums)):

            if nums[idx]:
                return idx

    def removeDuplicates(self, nums):

        self.mark(nums)

        print (nums)








r = Solution()
r.removeDuplicates([1,2,3,4,4,4,4,4,6])
