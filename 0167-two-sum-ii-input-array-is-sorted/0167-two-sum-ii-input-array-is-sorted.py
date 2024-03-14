class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        index = 1
        for val in numbers:
            if target - val in hashmap:
                return [hashmap[target-val],index]
            else:
                hashmap[val] = index
            index += 1