class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = nums.sort()
        length = len(nums)

        for i in range(1,length ):
            if nums[i] == nums[i-1]:
                return nums[i]
            
        