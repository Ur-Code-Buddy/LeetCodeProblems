class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left_arr, right_arr, res = [] , [] , []

        temp = 1
        for i in range(n):
            temp = nums[i] * temp
            left_arr.append(temp)
        
        temp = 1
        for i in range(n - 1, -1, -1):
            temp = nums[i] * temp
            right_arr.append(temp)
        right_arr.reverse()

        res.append(right_arr[1])
        for i in range(1,n - 1):
            res.append(left_arr[i - 1] * right_arr[i+1] )
        res.append(left_arr[n - 2])

        return res


        


