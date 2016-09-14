class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        acc = []

        l = len(nums)
        if l == 0:
            return []
        elif l == 1:
            return [str(nums[0])]
        else:
            acc = []
            t = [nums[0]]
            start = nums[0]

            for i,num in enumerate(nums[1:]):

                if start + 1  == num:
                    t.append(num)
                else:
                    acc.append(t)
                    t = [num]

                start = num

            final = acc + [t]
            joined = [str(x[0]) + '->' + str(x[-1]) if len(x) >= 2 else str(x[0]) for x in final]
            return joined

r = Solution()
res = r.summaryRanges([0,1,2,3,4,5,6, 10, 11])
print (res)

