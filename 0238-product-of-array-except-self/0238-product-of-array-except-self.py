class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        prefix = [1] * length
        postfix = [1] * length
        result = [1] * length

        for i in range(1,length):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(length - 2,-1,-1):
            postfix[i] = postfix[i+1] * nums[i+1]
            
        return [prefix[i] * postfix[i] for i in range(length)]

