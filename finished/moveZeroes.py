from collections import deque
class Solution(object):
    def moveZeroes(self, nums):

        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        queue = deque()
        list_len = 0
        queue_len = 0

        for num in nums:
            list_len += 1
            if num != 0:
                queue.append(num)
                queue_len += 1

        for i in range(list_len):

            nums[i] = queue.popleft() if queue_len > 0 else 0
            queue_len -= 1
