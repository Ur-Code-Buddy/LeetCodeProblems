class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left_arr, right_arr, res = [1] * n, [1] * n, [1] * n

        for i in range(1, n):
            left_arr[i] = left_arr[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            right_arr[i] = right_arr[i + 1] * nums[i + 1]

        for i in range(n):
            res[i] = left_arr[i] * right_arr[i]

        return res
