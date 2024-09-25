class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash_set = set()
        for val in nums:
            if val in hash_set:
                return True
            else:
                hash_set.add(val)
        return False
    


        