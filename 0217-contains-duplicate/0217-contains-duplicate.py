class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        print(len(set(nums)), len(nums) )

        if len(set(nums)) < len(nums):
            return True
        
        return False
        