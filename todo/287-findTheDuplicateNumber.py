class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = set()
        for num in nums:

            if num in d:
                return num

            d.add(num)
        



r  = Solution()

i = [1,4,4,2,4]

res = r.findDuplicate(i)

print (res)



