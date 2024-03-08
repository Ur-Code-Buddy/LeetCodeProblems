class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap = {}
        maximum = 0
        for val in nums:
            if val in hashmap:
                hashmap[val] += 1
            else:
                hashmap[val] = 1
            maximum = max(maximum, hashmap[val])

        result = 0
        for val, freq in hashmap.items():
            if freq == maximum:
                result += freq
        return result
