class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        hashmap = set()
        for i in nums:
            hashmap.add(i)
        if len(hashmap) != len(nums):
            return True
        return False