class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashset = set(nums)
        n = len(nums)
        for i in range(n + 1):
            if i not in hashset:
                return i
        