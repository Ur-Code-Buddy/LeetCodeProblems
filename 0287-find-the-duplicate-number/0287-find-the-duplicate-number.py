class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s, f = 0,0
        
        while(True):
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                break 
                
        start = 0
        
        while(True):
            if s == start:
                break
                
            s = nums[s]
            start = nums[start]
        return s
            
        
        