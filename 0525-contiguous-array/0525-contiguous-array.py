class Solution:
    def findMaxLength(self, nums):
        hashmap = {}
        maxlen = count = 0
        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count == 0:
                maxlen = i + 1
            if count in hashmap:
                maxlen = max(maxlen, i - hashmap[count])
            else:
                hashmap[count] = i
        return maxlen
