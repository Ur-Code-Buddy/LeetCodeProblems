class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        zeroCount = 0
        result = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroCount += 1
            while(zeroCount > k):
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1
            result = max(result, right - left + 1)
        return result
            