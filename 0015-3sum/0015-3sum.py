class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        length = len(nums)
        res = []
        
        for i in range(length):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            l = i + 1
            r = length - 1
            
            while (l < r):
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                        
                    l += 1
                    r -= 1
                    
                elif total < 0:
                    l += 1
                else:
                    r -= 1
                    
        return res
                        
        