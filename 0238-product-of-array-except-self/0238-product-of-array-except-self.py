class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prefix_products = [1] * n
        suffix_products = [1] * n
        result_list = [1] * n
        
        # Calculate prefix products
        prefix_product = 1
        for i in range(n):
            prefix_products[i] = prefix_product
            prefix_product *= nums[i]
        
        # Calculate suffix products
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            suffix_products[i] = suffix_product
            suffix_product *= nums[i]
        
        # Calculate final result
        for i in range(n):
            result_list[i] = prefix_products[i] * suffix_products[i]
        
        return result_list
