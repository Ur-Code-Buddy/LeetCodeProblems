class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        index = 0
        for val in nums:
            if target - val in hashmap:
                return [index,hashmap[target-val] ]
            else:
                hashmap[val] = index
                
            index += 1
                
        
                