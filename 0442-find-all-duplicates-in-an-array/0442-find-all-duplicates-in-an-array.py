class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        res = []
        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1]:
                res.append(nums[i])
            while(i < len(nums) and nums[i] == nums[i - 1]):
                i += 1
        return res
            
            