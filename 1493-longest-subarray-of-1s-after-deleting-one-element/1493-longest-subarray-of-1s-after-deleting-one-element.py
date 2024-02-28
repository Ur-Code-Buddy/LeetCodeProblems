class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        zeroCount = 0
        result = 0
        length = len(nums)
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroCount += 1
            while(zeroCount > 1):
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1
            result = max(result, right - left)
        if not result: return 0
        return result