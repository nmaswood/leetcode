class Solution(object):

    def removeDuplicates(self, nums):

        i = 0
        j = 0

        for index, num in enumerate(nums):

            if index + 1 == len(nums):
                nums[j] = num
                j += 1

            elif num < nums[index + 1]:

                nums[j] = num
                j += 1

        for k in range(j, len(nums)):

            nums[k] = None





ori = [1,2,2,3,3,3,4,4]
print (ori)
r = Solution()
res = r.removeDuplicates(ori)
print (ori)
