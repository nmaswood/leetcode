# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class BST():
    
    def __init__(self, key, left = None, right = None):
        self.root = key
        self.left = left
        self.right = right
    
    
    def ins(self, num):
        
        # f BST -> BST
        #
        #
        
        def f (tree,val):
            
            if not tree:
                return BST(val)
            
            val = root.val
            left, right = root.left, root.right
            
            if val == root.val:
                return BST(left, right)
            elif val >= root.val:
                return BST(left, f(right, val))
            else:
                return BST(f(left,val), right)
        
        self = self.ins(self, num)
        

class Solution(object):
    
    def createBST(self, nums):
        
        
        def f(nums):
        
            l = len(nums)
            if l == 0:
                return None
            elif l == 1:
                return BST(l[0])

            mid_point = l - 1 / 2
            left_half,right_half = nums[:mid_point], nums[mid_point:]

            center = nums[mid_point]

            return BST(createBST(left_half), createBST(right_half))
                       
       return f(nums)

         
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        nums = list(range(n))
        
        def f(nums):
            
            l = len(nums)
            if l == 0:
                assert False
            elif l == 1:
                return l[0]
            
            mid_point = l - 1 / 2
            
            if 
            
            
            
            
           if isBadVersion(n):
            return n 
            
           else
        
            
            
            
            
             
                       
                       
                       
        