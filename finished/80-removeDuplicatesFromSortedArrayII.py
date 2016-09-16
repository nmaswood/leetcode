class Solution(object):

    def mark(self, nums):
        print(nums)

        prev = nums[0]
        prevCounter = 1

        for index, num in enumerate(nums[1:]):

            if num == prev:

                if prevCounter == 2:
                    nums[index + 1] = None
                else:
                    prevCounter += 1
            else:
                prevCounter = 1

            prev = num

        return nums


    def next_dup(self, nums, i):

        for idx in range(i, len(nums)):

            if nums[idx]:
                return idx

    def removeDuplicates(self, nums):

        if nums == []:
            return

        nums = self.mark(nums)

        l = len([x for x in nums if x is not None])

        i = -1

        print (nums)
        for idx, num in enumerate(nums):

            if num is None:
                if i == -1:
                    i = idx
            else:
                if i != -1:
                    nums[i] = num
                    nums[idx] = None
                    i += 1
        print (nums)
        return l



r = Solution()
res = r.removeDuplicates([0,0,0,0,0,1,2,2,3,3,4,4,4, 5,5,5,5,5])
print (res)
