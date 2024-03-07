class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numset = set(nums)
        longest = 0
        current = 0
        for n in numset:
            if (n-1) not in numset:
                k = n
                current = 1
                while (k+1) in numset:
                    current += 1
                    k += 1
                if current > longest:
                    longest = current
        return longest