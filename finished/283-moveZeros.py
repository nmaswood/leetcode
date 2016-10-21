from collections import deque
"""
class Solution(object):
    def moveZeroes(self, nums):

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
"""

class Solution(object):

    def moveZeroes(self, nums):
        j = 0
        for n in nums:
            if n != 0:
                nums[j] = n
                j += 1
        while j < len(nums):
            nums[j] = 0
            j += 1

r = Solution()
a = [1,0,2,0,3, 0,0 ,1 ,2 ,3 ]
r.moveZeroes(a)
print (a)


