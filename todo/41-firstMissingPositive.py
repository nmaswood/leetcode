class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 1

        MIN = min(nums)
        MAX = max(nums)
        SUM = sum(nums)
        acc = 0

        for x in range(MIN, MAX + 1):
            acc+= x

        print ('acc', acc)
        print ('sum', SUM)
        print('res', acc - SUM)

        if acc - SUM == 0:
            if MIN != 0:
                return MIN - 1
            return MAX + 1

        return acc - SUM

r = Solution()
res = r.firstMissingPositive([1])
print (res)

