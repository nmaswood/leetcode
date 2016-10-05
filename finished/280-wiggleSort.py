class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        on = True

        l = len(nums)

        for index, num in enumerate(nums):

            if index == l - 1:
                continue


            next_number = nums[index + 1]

            if on:
                if num > next_number:
                    nums[index], nums[index + 1] = next_number, num
                on = False
            else:
                if num < next_number:
                    nums[index], nums[index + 1] = next_number, num
                on = True


x = [3,5,2, 1,6,4]
r = Solution()
res = r.wiggleSort(x)

print (x)

