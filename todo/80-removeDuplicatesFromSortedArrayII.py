class Solution(object):

    def mark(self, nums):

        prev = None
        prevCounter = 0

        t = 0

        for index, num in enumerate(nums):

            if num == prev:

                if prevCounter == 2:
                    nums[index] = None
                    t+=1
                    prev = 0
                else:
                    prevCounter += 1
            else:
                prev = 0

            prev = num

        return nums


    def next_dup(self, nums, i):

        for idx in range(i, len(nums)):

            if nums[idx]:
                return idx

    def removeDuplicates(self, nums):

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
res = r.removeDuplicates([0,0,0,0,0,1,2,2,3,3,4,4])
print (res)
