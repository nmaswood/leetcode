class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """


        len_1 = len(nums1)
        len_2 = len(nums1)

        for index, letter in range(len_2):

            nums1[index] = nums1[len_1 + index]
            nums1[index] = None

        def merge(num1index, index1, index2):

            if index1 == len_1 + len_2 and index2 == len_2:
                return

            if index1 == len_1 + len_2:
                nums1[num1index] = nums2[index2]
                return merge(num1index + 1 , index1, index2 + 1)

            if index2 == len_2:
                nums1[num1index] = nums2[index2]
                return merge(num1index + 1 , index1 + 1, index2)

            num1, num2 = nums1[index1], nums2[index2]

            if num1 < num2:

                nums1[num1index] = num1
                return merge(num1index + 1, index1 + 1, index2)

            else:
                nums1[num1index] = num2
                return merge(num1index + 1, index1 + 1, index2)

        merge(0, len_1, 0)


r = Solution()

r.merge([0], 1,[1], 2)
