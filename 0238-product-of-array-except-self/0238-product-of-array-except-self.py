class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        result = [1] * length
        temp = 1

        for i in range(length):
            result[i] *= temp
            temp *= nums[i]
        temp = 1
        for i in range(length - 1,-1,-1):
            result[i] *= temp
            temp *= nums[i]
        return result

