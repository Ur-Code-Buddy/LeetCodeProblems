class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        length = len(nums)
        rp = []
        res_arr = []
        
        temp = 1
        for i in range(length - 1,-1,-1):
            temp = temp * nums[i]
            rp.append(temp)
        rp.reverse()
        temp = 1
        for i in range(length):
            if i + 1 < length:
                res_arr.append( temp * rp[i + 1])
            else:
                res_arr.append(temp)
                
            temp *= nums[i]

        return res_arr
        