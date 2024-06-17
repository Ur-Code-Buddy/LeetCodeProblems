class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        length = len(nums)
        res_arr = [1] * length
        temp = 1
        
        for i in range(length):
            res_arr[i] = temp
            temp *= nums[i]
        
        temp = 1

        for i in range(length - 1, -1, -1):
            res_arr[i] *= temp
            temp *= nums[i]

        return res_arr