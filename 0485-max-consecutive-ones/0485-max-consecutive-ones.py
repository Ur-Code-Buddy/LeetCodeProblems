class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLength = 0
        currentLength = 0

        for i in nums:
            if i == 1:
                currentLength += 1
                if currentLength > maxLength:
                    maxLength = currentLength
            else: currentLength = 0
        
        return maxLength