class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = 0

        for i in nums:
            total_sum = total_sum ^ i
            
        return total_sum
        