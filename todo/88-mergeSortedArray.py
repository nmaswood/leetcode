class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        def ins(l, x):
            if not l:
                return [x]
            else:
                first = l[0]
                if x <= first:
                    return [x] + l
                else:
                    return [first] + ins(l[1:], x)

        for num in nums2:
            nums1 = ins(nums1, num)
        print (nums1)

r = Solution()

r.merge([0], 1,[1], 2)
