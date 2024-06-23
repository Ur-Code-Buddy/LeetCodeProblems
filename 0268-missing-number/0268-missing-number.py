class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # hashset = set(nums)
        # n = len(nums)
        # for i in range(n + 1):
        #     if i not in hashset:
        #         return i
        

        n = len(nums)
        total_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return total_sum - actual_sum