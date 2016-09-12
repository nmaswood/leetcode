class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        vals = range(lower, upper + 1)
        v = set(nums)
        init_list = list(nums)

        nums = (val for val in vals if val not in v)


        acc = []

        l = len(v)
        if l == 1:
            return []
        elif l == 0:
            x = next(nums)
            return [str(x)]
        else:
            acc = []

            x = next(nums)

            t = [x]
            start = x
            for i,num in enumerate(nums):

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
res = r.findMissingRanges([], 1,1)
print (res)

