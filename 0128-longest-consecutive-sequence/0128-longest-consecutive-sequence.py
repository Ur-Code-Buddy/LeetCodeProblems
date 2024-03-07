class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numset = set(nums)
        longest = 0
        for n in numset:
            if (n-1) not in numset:
                length = 1
                while (n+length) in numset:
                    length += 1
                if length > longest:
                    longest = length
        return longest