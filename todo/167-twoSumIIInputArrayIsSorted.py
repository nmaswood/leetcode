class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        l_index,r_index = 0, len(numbers) - 1



        while l_index < r_index:

            left = numbers[l_index]
            right = numbers[r_index]

            total = left + right

            if total == target:
                return l_index + 1, r_index + 1
            elif total > target:
                r_index -= 1
            else:
                l_index +=1

        return 0,0

#r = Solution()

#nums = [2,7,11,15]
#target = 9

#x =  r.twoSum(nums, target)
#print (x)
